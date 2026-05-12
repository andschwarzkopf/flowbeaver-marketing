#!/usr/bin/env python3
"""
Kampagnen-Phasen-Analyse fuer Flowbeaver Google Ads + GA4.

Eine Phase = eine Anzeigengruppe innerhalb einer Kampagne.
Phase-Zeitraum = vom ersten bis zum letzten Tag mit Impressions in dieser Anzeigengruppe.
Final URLs = alle URL-Versionen, die im Phase-Zeitraum aktiv waren.
GA4-Daten gefiltert auf Paid Search (sessionMedium = cpc) und Landingpage-Pfad.

Usage:
    source outbound/engine/.venv/bin/activate
    python3 scripts/campaign_phase_analysis.py

Output: paid-ads/reports/campaign-phase-analysis-YYYY-MM-DD.md
"""

import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

import requests
from google.oauth2.credentials import Credentials
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    RunReportRequest, DateRange, Dimension, Metric,
    FilterExpression, FilterExpressionList, Filter,
)
from google.ads.googleads.client import GoogleAdsClient

SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
START_DATE = '2024-01-01'


# === Config ===

def load_env():
    env_path = PROJECT_DIR / '.env'
    env = {}
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if '=' in line and not line.startswith('#'):
                key, val = line.split('=', 1)
                env[key.strip()] = val.strip()
    return env


def get_ga4_client(env):
    creds = Credentials(
        token=None,
        refresh_token=env['GOOGLE_REFRESH_TOKEN'],
        client_id=env['GOOGLE_CLIENT_ID'],
        client_secret=env['GOOGLE_CLIENT_SECRET'],
        token_uri='https://oauth2.googleapis.com/token',
    )
    return BetaAnalyticsDataClient(credentials=creds)


def get_ads_client(env):
    config = {
        'developer_token': env['GOOGLE_ADS_DEVELOPER_TOKEN'],
        'client_id': env['GOOGLE_CLIENT_ID'],
        'client_secret': env['GOOGLE_CLIENT_SECRET'],
        'refresh_token': env['GOOGLE_REFRESH_TOKEN'],
        'use_proto_plus': True,
    }
    return GoogleAdsClient.load_from_dict(config)


# === Google Ads queries ===

def fetch_campaign_overview(ads_client, customer_id, end_date):
    ga = ads_client.get_service("GoogleAdsService")
    query = f"""
        SELECT
          campaign.id, campaign.name, campaign.status,
          campaign.advertising_channel_type,
          metrics.impressions, metrics.clicks, metrics.cost_micros,
          metrics.conversions, metrics.conversions_value,
          segments.date
        FROM campaign
        WHERE segments.date BETWEEN '{START_DATE}' AND '{end_date}'
    """
    campaigns = {}
    for row in ga.search(customer_id=customer_id, query=query):
        cid = str(row.campaign.id)
        date = row.segments.date
        if cid not in campaigns:
            campaigns[cid] = {
                'id': cid,
                'name': row.campaign.name,
                'status': row.campaign.status.name,
                'channel_type': row.campaign.advertising_channel_type.name,
                'first_active': date, 'last_active': date,
                'impressions': 0, 'clicks': 0, 'cost': 0.0,
                'conversions': 0.0, 'conv_value': 0.0,
            }
        if date < campaigns[cid]['first_active']:
            campaigns[cid]['first_active'] = date
        if date > campaigns[cid]['last_active']:
            campaigns[cid]['last_active'] = date
        c = campaigns[cid]
        c['impressions'] += row.metrics.impressions
        c['clicks'] += row.metrics.clicks
        c['cost'] += row.metrics.cost_micros / 1_000_000
        c['conversions'] += row.metrics.conversions
        c['conv_value'] += row.metrics.conversions_value
    return campaigns


def fetch_ad_phases(ads_client, customer_id, end_date):
    """Per-day metrics fuer jede Anzeige, gruppiert nach (campaign, ad_group)."""
    ga = ads_client.get_service("GoogleAdsService")
    query = f"""
        SELECT
          campaign.id, campaign.name,
          ad_group.id, ad_group.name, ad_group.status,
          ad_group_ad.ad.id,
          ad_group_ad.status,
          ad_group_ad.ad.type,
          ad_group_ad.ad.responsive_search_ad.headlines,
          ad_group_ad.ad.responsive_search_ad.descriptions,
          ad_group_ad.ad.expanded_text_ad.headline_part1,
          ad_group_ad.ad.expanded_text_ad.headline_part2,
          ad_group_ad.ad.expanded_text_ad.description,
          ad_group_ad.ad.final_urls,
          segments.date,
          metrics.impressions, metrics.clicks, metrics.cost_micros, metrics.conversions
        FROM ad_group_ad
        WHERE segments.date BETWEEN '{START_DATE}' AND '{end_date}'
          AND metrics.impressions > 0
    """
    phases = {}
    for row in ga.search(customer_id=customer_id, query=query):
        cid = str(row.campaign.id)
        agid = str(row.ad_group.id)
        ad_id = str(row.ad_group_ad.ad.id)
        date = row.segments.date

        key = (cid, agid)
        if key not in phases:
            phases[key] = {
                'campaign_id': cid,
                'campaign_name': row.campaign.name,
                'ad_group_id': agid,
                'ad_group_name': row.ad_group.name,
                'ad_group_status': row.ad_group.status.name,
                'first_date': date, 'last_date': date,
                'impressions': 0, 'clicks': 0, 'cost': 0.0, 'conversions': 0.0,
                'ads': {},
                'final_urls': set(),
            }
        p = phases[key]
        if date < p['first_date']:
            p['first_date'] = date
        if date > p['last_date']:
            p['last_date'] = date
        p['impressions'] += row.metrics.impressions
        p['clicks'] += row.metrics.clicks
        p['cost'] += row.metrics.cost_micros / 1_000_000
        p['conversions'] += row.metrics.conversions

        if ad_id not in p['ads']:
            ad = row.ad_group_ad.ad
            ad_type = ad.type_.name if hasattr(ad, 'type_') else ad.type.name
            headlines, descriptions = [], []
            if ad_type == 'RESPONSIVE_SEARCH_AD':
                headlines = [h.text for h in ad.responsive_search_ad.headlines]
                descriptions = [d.text for d in ad.responsive_search_ad.descriptions]
            elif ad_type == 'EXPANDED_TEXT_AD':
                h1 = ad.expanded_text_ad.headline_part1
                h2 = ad.expanded_text_ad.headline_part2
                headlines = [h for h in [h1, h2] if h]
                if ad.expanded_text_ad.description:
                    descriptions = [ad.expanded_text_ad.description]
            p['ads'][ad_id] = {
                'id': ad_id, 'type': ad_type,
                'status': row.ad_group_ad.status.name,
                'headlines': headlines, 'descriptions': descriptions,
                'final_urls': list(ad.final_urls),
                'first_date': date, 'last_date': date,
                'impressions': 0, 'clicks': 0, 'cost': 0.0, 'conversions': 0.0,
            }
        a = p['ads'][ad_id]
        a['impressions'] += row.metrics.impressions
        a['clicks'] += row.metrics.clicks
        a['cost'] += row.metrics.cost_micros / 1_000_000
        a['conversions'] += row.metrics.conversions
        if date < a['first_date']:
            a['first_date'] = date
        if date > a['last_date']:
            a['last_date'] = date

        for u in ad.final_urls:
            p['final_urls'].add(u)
    return phases


def fetch_keywords_per_adgroup(ads_client, customer_id, end_date):
    ga = ads_client.get_service("GoogleAdsService")
    query = f"""
        SELECT
          campaign.id, ad_group.id,
          ad_group_criterion.keyword.text,
          ad_group_criterion.keyword.match_type,
          ad_group_criterion.status,
          metrics.impressions, metrics.clicks, metrics.cost_micros,
          metrics.conversions, metrics.ctr, metrics.average_cpc
        FROM keyword_view
        WHERE segments.date BETWEEN '{START_DATE}' AND '{end_date}'
          AND metrics.impressions > 0
    """
    keywords = defaultdict(list)
    for row in ga.search(customer_id=customer_id, query=query):
        key = (str(row.campaign.id), str(row.ad_group.id))
        keywords[key].append({
            'text': row.ad_group_criterion.keyword.text,
            'match_type': row.ad_group_criterion.keyword.match_type.name,
            'status': row.ad_group_criterion.status.name,
            'impressions': row.metrics.impressions,
            'clicks': row.metrics.clicks,
            'cost': row.metrics.cost_micros / 1_000_000,
            'conversions': row.metrics.conversions,
            'ctr': row.metrics.ctr,
            'avg_cpc': row.metrics.average_cpc / 1_000_000,
        })
    return keywords


def fetch_search_terms_per_adgroup(ads_client, customer_id, end_date):
    """Top Suchbegriffe pro Anzeigengruppe (zeigt was tatsaechlich gesucht wurde)."""
    ga = ads_client.get_service("GoogleAdsService")
    query = f"""
        SELECT
          campaign.id, ad_group.id,
          search_term_view.search_term,
          metrics.impressions, metrics.clicks, metrics.cost_micros,
          metrics.conversions, metrics.ctr
        FROM search_term_view
        WHERE segments.date BETWEEN '{START_DATE}' AND '{end_date}'
          AND metrics.impressions > 0
    """
    terms = defaultdict(list)
    for row in ga.search(customer_id=customer_id, query=query):
        key = (str(row.campaign.id), str(row.ad_group.id))
        terms[key].append({
            'text': row.search_term_view.search_term,
            'impressions': row.metrics.impressions,
            'clicks': row.metrics.clicks,
            'cost': row.metrics.cost_micros / 1_000_000,
            'conversions': row.metrics.conversions,
            'ctr': row.metrics.ctr,
        })
    return terms


# === GA4 ===

def url_to_path(url):
    p = urlparse(url)
    return p.path or '/'


def fetch_ga4_for_url(ga4_client, prop, url_path, start, end):
    try:
        request = RunReportRequest(
            property=prop,
            date_ranges=[DateRange(start_date=start, end_date=end)],
            metrics=[
                Metric(name='sessions'),
                Metric(name='totalUsers'),
                Metric(name='bounceRate'),
                Metric(name='averageSessionDuration'),
                Metric(name='conversions'),
                Metric(name='screenPageViews'),
            ],
            dimensions=[Dimension(name='landingPage')],
            dimension_filter=FilterExpression(
                and_group=FilterExpressionList(expressions=[
                    FilterExpression(filter=Filter(
                        field_name='landingPage',
                        string_filter=Filter.StringFilter(
                            value=url_path,
                            match_type=Filter.StringFilter.MatchType.EXACT,
                        ),
                    )),
                    FilterExpression(filter=Filter(
                        field_name='sessionMedium',
                        string_filter=Filter.StringFilter(
                            value='cpc',
                            match_type=Filter.StringFilter.MatchType.EXACT,
                        ),
                    )),
                ]),
            ),
            limit=10,
        )
        response = ga4_client.run_report(request)
        if not response.rows:
            return {'sessions': 0, 'users': 0, 'bounce': 0, 'duration': 0, 'conversions': 0, 'pageviews': 0}
        total = {'sessions': 0, 'users': 0, 'bounce_sum': 0.0, 'duration_sum': 0.0, 'conversions': 0, 'pageviews': 0, 'rows': 0}
        for row in response.rows:
            mvs = row.metric_values
            total['sessions'] += int(float(mvs[0].value or 0))
            total['users'] += int(float(mvs[1].value or 0))
            total['bounce_sum'] += float(mvs[2].value or 0)
            total['duration_sum'] += float(mvs[3].value or 0)
            total['conversions'] += int(float(mvs[4].value or 0))
            total['pageviews'] += int(float(mvs[5].value or 0))
            total['rows'] += 1
        return {
            'sessions': total['sessions'],
            'users': total['users'],
            'bounce': total['bounce_sum'] / max(total['rows'], 1),
            'duration': total['duration_sum'] / max(total['rows'], 1),
            'conversions': total['conversions'],
            'pageviews': total['pageviews'],
        }
    except Exception as e:
        return {'error': str(e)}


# === Landing page snippets ===

def fetch_landing_page_snippet(url):
    try:
        r = requests.get(url, timeout=10, headers={
            'User-Agent': 'Mozilla/5.0 (compatible; FlowbeaverAnalysis/1.0)',
        }, allow_redirects=True)
        final_url = r.url
        status = r.status_code
        if status != 200:
            return {'status': status, 'final_url': final_url, 'error': f'HTTP {status}'}
        html = r.text

        title_m = re.search(r'<title[^>]*>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
        title = re.sub(r'\s+', ' ', title_m.group(1)).strip() if title_m else ''

        h1_m = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.IGNORECASE | re.DOTALL)
        h1_raw = h1_m.group(1) if h1_m else ''
        h1 = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', h1_raw)).strip()

        meta_m = re.search(
            r'<meta\s+name=["\']description["\']\s+content=["\']([^"\']+)["\']',
            html, re.IGNORECASE,
        )
        meta_desc = meta_m.group(1).strip() if meta_m else ''

        body_m = re.search(r'<body[^>]*>(.*?)</body>', html, re.IGNORECASE | re.DOTALL)
        if body_m:
            body = body_m.group(1)
            body = re.sub(r'<script.*?</script>', '', body, flags=re.IGNORECASE | re.DOTALL)
            body = re.sub(r'<style.*?</style>', '', body, flags=re.IGNORECASE | re.DOTALL)
            body = re.sub(r'<[^>]+>', ' ', body)
            body = re.sub(r'\s+', ' ', body).strip()
            preview = body[:400]
        else:
            preview = ''

        return {
            'status': status,
            'final_url': final_url,
            'title': title,
            'h1': h1,
            'meta_description': meta_desc,
            'preview': preview,
        }
    except Exception as e:
        return {'error': str(e)}


# === Formatting helpers ===

def fmt_eur(v):
    return f"{v:,.2f} EUR".replace(',', 'X').replace('.', ',').replace('X', '.')


def fmt_int(v):
    return f"{int(v):,}".replace(',', '.')


def fmt_pct(v):
    if v < 1.0001:
        v = v * 100
    return f"{v:.1f}%".replace('.', ',')


def fmt_dur(s):
    s = float(s)
    m, sec = divmod(int(s), 60)
    return f"{m}:{sec:02d}"


def fmt_conv(v):
    if v == 0:
        return '0'
    if abs(v - round(v)) < 0.001:
        return str(int(round(v)))
    return f"{v:.2f}".replace('.', ',')


# === Markdown rendering ===

def render_markdown(campaigns, phases, keywords, search_terms, ga4_data, snippets, end_date):
    lines = []
    lines.append(f"# Kampagnen-Phasen-Analyse — Stand {end_date}")
    lines.append('')
    lines.append(f"**Zeitraum:** {START_DATE} bis {end_date}")
    lines.append('')
    lines.append("## Kontext (fuer Claude-Chat-Analyse)")
    lines.append('')
    lines.append("**Produkt:** Flowbeaver — KI-Vorsystem fuer die vorbereitende Buchhaltung in Steuerkanzleien. ")
    lines.append("Kombination aus LLM, KI-OCR und deterministischen Regeln. Output: DATEV-kompatibler Buchungsstapel. ")
    lines.append("Flowbeaver ist eine **DATEV-Ergaenzung**, niemals eine DATEV-Alternative.")
    lines.append('')
    lines.append("**ICP:** Wachstumsorientierte Steuerkanzleien mit 4-10 Mitarbeitern. ")
    lines.append("Validierter Insight: Rueckfragen mit Mandanten sind der groesste Zeitkiller (nicht das Abtippen). ")
    lines.append("Flowbeaver-Differenzierung: LLM versteht jede Sprache und leitet aus exotischen Rechnungen klare Geschaeftsvorfaelle ab.")
    lines.append('')
    lines.append("**Aktuelle Kampagnen-Regeln:** Nur Exact-Match Keywords, kein Display, kein PMax, ")
    lines.append("Anzeigentexte muessen 'Steuerkanzlei' oder 'Kanzlei' enthalten.")
    lines.append('')
    lines.append("## Methodik")
    lines.append('')
    lines.append("Eine **Phase** = eine **Anzeigengruppe** innerhalb einer Kampagne. ")
    lines.append("Phase-Zeitraum = vom ersten bis zum letzten Tag mit Impressions in dieser Anzeigengruppe.")
    lines.append('')
    lines.append("**Final URLs** = alle URL-Versionen, die in der Phase aktiv waren (auch wenn ueber die Lebensdauer mehrere Anzeigen mit verschiedenen URLs liefen).")
    lines.append('')
    lines.append("**GA4-Daten** sind gefiltert auf:")
    lines.append("- `landingPage` (Pfad-only, exakte Uebereinstimmung)")
    lines.append("- `sessionMedium = cpc` (also nur Paid-Search-Traffic)")
    lines.append("- Phase-Zeitraum")
    lines.append('')
    lines.append("**Limitation:** GA4-Bounce-Rate und Avg-Dauer sind Durchschnitt der Tagesbuckets, nicht echte Phase-Aggregate. Sessions/Users/Conversions/Pageviews sind Summen. ")
    lines.append("Google-Ads-`change_event`-API ist auf 30 Tage Historie begrenzt — granulare Aenderungen vor April 2026 lassen sich nicht rekonstruieren.")
    lines.append('')
    lines.append('---')
    lines.append('')

    sorted_campaigns = sorted(campaigns.values(), key=lambda c: c['cost'], reverse=True)

    lines.append("## Kampagnen-Uebersicht")
    lines.append('')
    lines.append("| Kampagne | Status | Channel | Spend | Impr | Klicks | CTR | Conv | CPA |")
    lines.append("|---|---|---|---|---|---|---|---|---|")
    for c in sorted_campaigns:
        ctr = (c['clicks'] / c['impressions'] * 100) if c['impressions'] > 0 else 0
        cpa = (c['cost'] / c['conversions']) if c['conversions'] > 0 else 0
        lines.append(
            f"| {c['name']} | {c['status']} | {c['channel_type']} | {fmt_eur(c['cost'])} | "
            f"{fmt_int(c['impressions'])} | {fmt_int(c['clicks'])} | {ctr:.2f}% | "
            f"{fmt_conv(c['conversions'])} | {fmt_eur(cpa) if cpa else '—'} |"
        )
    lines.append('')

    total_spend = sum(c['cost'] for c in campaigns.values())
    total_clicks = sum(c['clicks'] for c in campaigns.values())
    total_impr = sum(c['impressions'] for c in campaigns.values())
    total_conv = sum(c['conversions'] for c in campaigns.values())
    lines.append(f"**Gesamt:** {fmt_eur(total_spend)} Spend, {fmt_int(total_impr)} Impressions, "
                 f"{fmt_int(total_clicks)} Klicks, {fmt_conv(total_conv)} Conversions")
    lines.append('')
    lines.append('---')
    lines.append('')

    for c in sorted_campaigns:
        lines.append(f"## Kampagne: {c['name']}")
        lines.append('')
        lines.append(f"- **Status:** {c['status']}")
        lines.append(f"- **Channel Type:** {c['channel_type']}")
        lines.append(f"- **Aktiv (mit Impressions):** {c.get('first_active') or '—'} bis {c.get('last_active') or '—'}")
        lines.append(f"- **Total Spend:** {fmt_eur(c['cost'])}")
        ctr = (c['clicks'] / c['impressions'] * 100) if c['impressions'] > 0 else 0
        cpc = (c['cost'] / c['clicks']) if c['clicks'] > 0 else 0
        cpa = (c['cost'] / c['conversions']) if c['conversions'] > 0 else 0
        lines.append(f"- **Impressions:** {fmt_int(c['impressions'])} / **Klicks:** {fmt_int(c['clicks'])} / **CTR:** {ctr:.2f}% / **Avg CPC:** {fmt_eur(cpc)}")
        lines.append(f"- **Conversions:** {fmt_conv(c['conversions'])} / **CPA:** {fmt_eur(cpa) if cpa else '—'}")
        lines.append('')

        c_phases = sorted(
            [p for p in phases.values() if p['campaign_id'] == c['id']],
            key=lambda p: p['first_date']
        )

        if not c_phases:
            lines.append("_Keine Anzeigen-Aktivitaet in dieser Kampagne._")
            lines.append('')
            lines.append('---')
            lines.append('')
            continue

        for i, p in enumerate(c_phases, 1):
            lines.append(f'### Phase {i}: Anzeigengruppe "{p["ad_group_name"]}"')
            lines.append('')
            d1 = datetime.strptime(p['first_date'], '%Y-%m-%d')
            d2 = datetime.strptime(p['last_date'], '%Y-%m-%d')
            days = (d2 - d1).days + 1
            lines.append(f"- **Zeitraum:** {p['first_date']} bis {p['last_date']} ({days} Tage)")
            lines.append(f"- **Anzeigengruppen-Status:** {p['ad_group_status']}")
            ctr = (p['clicks'] / p['impressions'] * 100) if p['impressions'] > 0 else 0
            cpc = (p['cost'] / p['clicks']) if p['clicks'] > 0 else 0
            cpa = (p['cost'] / p['conversions']) if p['conversions'] > 0 else 0
            lines.append(f"- **Spend:** {fmt_eur(p['cost'])} / Impr: {fmt_int(p['impressions'])} / Klicks: {fmt_int(p['clicks'])}")
            lines.append(f"- **CTR:** {ctr:.2f}% / **Avg CPC:** {fmt_eur(cpc)}")
            lines.append(f"- **Conversions:** {fmt_conv(p['conversions'])} / **CPA:** {fmt_eur(cpa) if cpa else '—'}")
            lines.append('')

            lines.append(f"#### Final URLs ({len(p['final_urls'])})")
            lines.append('')
            for u in sorted(p['final_urls']):
                lines.append(f"- `{u}`")
            lines.append('')

            lines.append(f"#### Anzeigen ({len(p['ads'])})")
            lines.append('')
            for ad in sorted(p['ads'].values(), key=lambda a: -a['impressions']):
                ad_ctr = (ad['clicks'] / ad['impressions'] * 100) if ad['impressions'] > 0 else 0
                lines.append(f"**Ad-ID {ad['id']}** ({ad['type']}, Status: {ad['status']})")
                lines.append(f"- Aktiv: {ad['first_date']} bis {ad['last_date']}")
                lines.append(f"- Spend: {fmt_eur(ad['cost'])} / Impr: {fmt_int(ad['impressions'])} / Klicks: {fmt_int(ad['clicks'])} / CTR: {ad_ctr:.2f}% / Conv: {fmt_conv(ad['conversions'])}")
                if ad['headlines']:
                    lines.append(f"- **Headlines:**")
                    for h in ad['headlines']:
                        lines.append(f"  - {h}")
                if ad['descriptions']:
                    lines.append(f"- **Descriptions:**")
                    for d in ad['descriptions']:
                        lines.append(f"  - {d}")
                if ad['final_urls']:
                    lines.append(f"- **Ad-spezifische Final URLs:** {', '.join(ad['final_urls'])}")
                lines.append('')

            kw_key = (c['id'], p['ad_group_id'])
            kws = keywords.get(kw_key, [])
            if kws:
                lines.append(f"#### Keywords ({len(kws)})")
                lines.append('')
                lines.append("| Keyword | Match | Status | Impr | Klicks | CTR | Avg CPC | Spend | Conv |")
                lines.append("|---|---|---|---|---|---|---|---|---|")
                for kw in sorted(kws, key=lambda k: -k['impressions']):
                    lines.append(
                        f"| {kw['text']} | {kw['match_type']} | {kw['status']} | "
                        f"{fmt_int(kw['impressions'])} | {fmt_int(kw['clicks'])} | "
                        f"{fmt_pct(kw['ctr'])} | {fmt_eur(kw['avg_cpc'])} | "
                        f"{fmt_eur(kw['cost'])} | {fmt_conv(kw['conversions'])} |"
                    )
                lines.append('')

            st = search_terms.get(kw_key, [])
            if st:
                top_st = sorted(st, key=lambda s: -s['impressions'])[:20]
                lines.append(f"#### Top-Suchbegriffe ({min(20, len(st))} von {len(st)})")
                lines.append('')
                lines.append("| Suchbegriff | Impr | Klicks | CTR | Spend | Conv |")
                lines.append("|---|---|---|---|---|---|")
                for s in top_st:
                    lines.append(
                        f"| {s['text']} | {fmt_int(s['impressions'])} | {fmt_int(s['clicks'])} | "
                        f"{fmt_pct(s['ctr'])} | {fmt_eur(s['cost'])} | {fmt_conv(s['conversions'])} |"
                    )
                lines.append('')

            lines.append("#### GA4 je Final-URL (Paid Search, Phase-Zeitraum)")
            lines.append('')
            lines.append("| URL-Pfad | Sessions | Users | Bounce | Avg Dauer | Conversions | Pageviews |")
            lines.append("|---|---|---|---|---|---|---|")
            for u in sorted(p['final_urls']):
                path = url_to_path(u)
                ga = ga4_data.get((p['campaign_id'], p['ad_group_id'], u), {})
                if 'error' in ga:
                    lines.append(f"| `{path}` | _{ga['error']}_ |  |  |  |  |  |")
                else:
                    lines.append(
                        f"| `{path}` | {fmt_int(ga.get('sessions', 0))} | {fmt_int(ga.get('users', 0))} | "
                        f"{fmt_pct(ga.get('bounce', 0))} | {fmt_dur(ga.get('duration', 0))} | "
                        f"{fmt_int(ga.get('conversions', 0))} | {fmt_int(ga.get('pageviews', 0))} |"
                    )
            lines.append('')

            lines.append("#### Landingpage-Snippets (aktueller Stand)")
            lines.append('')
            for u in sorted(p['final_urls']):
                snip = snippets.get(u, {})
                lines.append(f"**{u}**")
                if 'error' in snip:
                    redir = f" (final: {snip.get('final_url', '—')})" if snip.get('final_url') and snip.get('final_url') != u else ''
                    lines.append(f"- Status: {snip.get('error', 'unbekannt')}{redir}")
                else:
                    if snip.get('final_url') and snip['final_url'] != u:
                        lines.append(f"- **Redirect zu:** {snip['final_url']}")
                    lines.append(f"- **Title:** {snip.get('title') or '—'}")
                    lines.append(f"- **H1:** {snip.get('h1') or '—'}")
                    lines.append(f"- **Meta Description:** {snip.get('meta_description') or '—'}")
                    if snip.get('preview'):
                        lines.append(f"- **Preview:** {snip['preview']}")
                lines.append('')

        lines.append('---')
        lines.append('')

    return '\n'.join(lines)


# === Main ===

def main():
    end_date = datetime.now().strftime('%Y-%m-%d')
    print(f"Kampagnen-Phasen-Analyse {START_DATE} bis {end_date}\n", flush=True)

    env = load_env()
    ga4_client = get_ga4_client(env)
    ads_client = get_ads_client(env)
    customer_id = env['GOOGLE_ADS_CUSTOMER_ID'].replace('-', '')
    prop = f"properties/{env['GA4_PROPERTY_ID']}"

    print("[Ads] Lade Kampagnen-Uebersicht...", flush=True)
    campaigns = fetch_campaign_overview(ads_client, customer_id, end_date)
    print(f"  -> {len(campaigns)} Kampagnen", flush=True)

    print("[Ads] Lade Anzeigen-Performance pro Tag (kann ein paar Sekunden dauern)...", flush=True)
    phases = fetch_ad_phases(ads_client, customer_id, end_date)
    print(f"  -> {len(phases)} Anzeigengruppen-Phasen", flush=True)

    print("[Ads] Lade Keywords je Anzeigengruppe...", flush=True)
    keywords = fetch_keywords_per_adgroup(ads_client, customer_id, end_date)
    print(f"  -> Keywords fuer {len(keywords)} Anzeigengruppen", flush=True)

    print("[Ads] Lade Suchbegriffe je Anzeigengruppe...", flush=True)
    search_terms = fetch_search_terms_per_adgroup(ads_client, customer_id, end_date)
    print(f"  -> Suchbegriffe fuer {len(search_terms)} Anzeigengruppen", flush=True)

    all_url_phase_pairs = []
    for key, p in phases.items():
        for u in p['final_urls']:
            all_url_phase_pairs.append((key[0], key[1], u, p['first_date'], p['last_date'], p['ad_group_name']))

    print(f"[GA4] Lade Daten fuer {len(all_url_phase_pairs)} (Phase, URL)-Kombinationen...", flush=True)
    ga4_data = {}
    for cid, agid, u, first_d, last_d, ag_name in all_url_phase_pairs:
        path = url_to_path(u)
        print(f"  - [{ag_name[:40]}] {path}", flush=True)
        ga4_data[(cid, agid, u)] = fetch_ga4_for_url(ga4_client, prop, path, first_d, last_d)

    all_urls = set()
    for p in phases.values():
        all_urls.update(p['final_urls'])
    print(f"\n[Web] Lade Landingpage-Snippets fuer {len(all_urls)} URLs...", flush=True)
    snippets = {}
    for u in sorted(all_urls):
        print(f"  - {u}", flush=True)
        snippets[u] = fetch_landing_page_snippet(u)

    print("\nGeneriere Markdown-Report...", flush=True)
    md = render_markdown(campaigns, phases, keywords, search_terms, ga4_data, snippets, end_date)
    out_path = PROJECT_DIR / 'paid-ads' / 'reports' / f'campaign-phase-analysis-{end_date}.md'
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(md, encoding='utf-8')

    size_kb = len(md.encode('utf-8')) / 1024
    print(f"\nReport gespeichert: {out_path}")
    print(f"Groesse: {size_kb:.1f} KB / {len(md.splitlines())} Zeilen")


if __name__ == '__main__':
    main()
