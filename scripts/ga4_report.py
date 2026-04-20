#!/usr/bin/env python3
"""
GA4 + Google Ads Reporting — Erstellt Weekly, Monthly und Historical HTML-Reports.

Usage:
    python3 scripts/ga4_report.py weekly
    python3 scripts/ga4_report.py monthly
    python3 scripts/ga4_report.py historical
    python3 scripts/ga4_report.py all
"""

import os
import sys
import json
from datetime import datetime, timedelta
from pathlib import Path
from google.oauth2.credentials import Credentials
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    RunReportRequest, DateRange, Dimension, Metric, OrderBy, FilterExpression,
    Filter
)

# --- Config ---

SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
REPORTS_DIR = PROJECT_DIR / 'paid-ads' / 'reports'

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

def get_property_id(env):
    return f"properties/{env['GA4_PROPERTY_ID']}"

def get_ads_client(env):
    from google.ads.googleads.client import GoogleAdsClient
    config = {
        'developer_token': env['GOOGLE_ADS_DEVELOPER_TOKEN'],
        'client_id': env['GOOGLE_CLIENT_ID'],
        'client_secret': env['GOOGLE_CLIENT_SECRET'],
        'refresh_token': env['GOOGLE_REFRESH_TOKEN'],
        'use_proto_plus': True,
    }
    return GoogleAdsClient.load_from_dict(config)

def get_ads_customer_id(env):
    return env['GOOGLE_ADS_CUSTOMER_ID'].replace('-', '')


# --- GA4 Data Fetching ---

def fetch_report(client, property_id, date_ranges, dimensions, metrics, limit=50):
    request = RunReportRequest(
        property=property_id,
        date_ranges=date_ranges,
        dimensions=[Dimension(name=d) for d in dimensions],
        metrics=[Metric(name=m) for m in metrics],
        limit=limit,
    )
    return client.run_report(request)

def fetch_traffic_overview(client, prop, date_range):
    return fetch_report(
        client, prop, [date_range],
        dimensions=['date'],
        metrics=['sessions', 'totalUsers', 'newUsers', 'screenPageViews',
                 'averageSessionDuration', 'bounceRate', 'conversions'],
        limit=366,
    )

def fetch_traffic_sources(client, prop, date_range):
    return fetch_report(
        client, prop, [date_range],
        dimensions=['sessionDefaultChannelGroup'],
        metrics=['sessions', 'totalUsers', 'conversions', 'bounceRate'],
        limit=20,
    )

def fetch_landing_pages(client, prop, date_range):
    return fetch_report(
        client, prop, [date_range],
        dimensions=['landingPagePlusQueryString'],
        metrics=['sessions', 'totalUsers', 'conversions', 'bounceRate',
                 'averageSessionDuration'],
        limit=30,
    )

def fetch_devices(client, prop, date_range):
    return fetch_report(
        client, prop, [date_range],
        dimensions=['deviceCategory'],
        metrics=['sessions', 'totalUsers', 'conversions'],
        limit=10,
    )

def fetch_geo(client, prop, date_range):
    return fetch_report(
        client, prop, [date_range],
        dimensions=['country'],
        metrics=['sessions', 'totalUsers', 'conversions'],
        limit=15,
    )

def fetch_conversions_by_source(client, prop, date_range):
    return fetch_report(
        client, prop, [date_range],
        dimensions=['sessionDefaultChannelGroup', 'sessionSourceMedium'],
        metrics=['conversions', 'sessions', 'totalUsers'],
        limit=30,
    )


# --- Google Ads Data Fetching ---

def fetch_ads_campaign_performance(ads_client, customer_id, start_date, end_date):
    ga_service = ads_client.get_service("GoogleAdsService")
    query = f"""
        SELECT
            campaign.name,
            campaign.status,
            metrics.impressions,
            metrics.clicks,
            metrics.cost_micros,
            metrics.conversions,
            metrics.conversions_value,
            metrics.ctr,
            metrics.average_cpc,
            metrics.cost_per_conversion
        FROM campaign
        WHERE segments.date BETWEEN '{start_date}' AND '{end_date}'
            AND campaign.status != 'REMOVED'
        ORDER BY metrics.cost_micros DESC
    """
    rows = []
    response = ga_service.search(customer_id=customer_id, query=query)
    for row in response:
        rows.append({
            'campaign': row.campaign.name,
            'status': row.campaign.status.name,
            'impressions': row.metrics.impressions,
            'clicks': row.metrics.clicks,
            'cost': row.metrics.cost_micros / 1_000_000,
            'conversions': row.metrics.conversions,
            'conv_value': row.metrics.conversions_value,
            'ctr': row.metrics.ctr,
            'avg_cpc': row.metrics.average_cpc / 1_000_000,
            'cost_per_conv': row.metrics.cost_per_conversion / 1_000_000 if row.metrics.cost_per_conversion > 0 else 0,
        })
    return rows

def fetch_ads_keyword_performance(ads_client, customer_id, start_date, end_date):
    ga_service = ads_client.get_service("GoogleAdsService")
    query = f"""
        SELECT
            ad_group_criterion.keyword.text,
            ad_group_criterion.keyword.match_type,
            campaign.name,
            metrics.impressions,
            metrics.clicks,
            metrics.cost_micros,
            metrics.conversions,
            metrics.ctr,
            metrics.average_cpc,
            metrics.search_impression_share
        FROM keyword_view
        WHERE segments.date BETWEEN '{start_date}' AND '{end_date}'
        ORDER BY metrics.impressions DESC
        LIMIT 30
    """
    rows = []
    response = ga_service.search(customer_id=customer_id, query=query)
    for row in response:
        rows.append({
            'keyword': row.ad_group_criterion.keyword.text,
            'match_type': row.ad_group_criterion.keyword.match_type.name,
            'campaign': row.campaign.name,
            'impressions': row.metrics.impressions,
            'clicks': row.metrics.clicks,
            'cost': row.metrics.cost_micros / 1_000_000,
            'conversions': row.metrics.conversions,
            'ctr': row.metrics.ctr,
            'avg_cpc': row.metrics.average_cpc / 1_000_000,
            'impression_share': row.metrics.search_impression_share,
        })
    return rows

def fetch_ads_search_terms(ads_client, customer_id, start_date, end_date):
    ga_service = ads_client.get_service("GoogleAdsService")
    query = f"""
        SELECT
            search_term_view.search_term,
            campaign.name,
            metrics.impressions,
            metrics.clicks,
            metrics.cost_micros,
            metrics.conversions,
            metrics.ctr
        FROM search_term_view
        WHERE segments.date BETWEEN '{start_date}' AND '{end_date}'
        ORDER BY metrics.impressions DESC
        LIMIT 30
    """
    rows = []
    response = ga_service.search(customer_id=customer_id, query=query)
    for row in response:
        rows.append({
            'search_term': row.search_term_view.search_term,
            'campaign': row.campaign.name,
            'impressions': row.metrics.impressions,
            'clicks': row.metrics.clicks,
            'cost': row.metrics.cost_micros / 1_000_000,
            'conversions': row.metrics.conversions,
            'ctr': row.metrics.ctr,
        })
    return rows

def fetch_ads_campaign_by_month(ads_client, customer_id, start_date, end_date):
    """Fetch campaign performance broken down by month for historical view."""
    ga_service = ads_client.get_service("GoogleAdsService")
    query = f"""
        SELECT
            campaign.name,
            segments.month,
            metrics.impressions,
            metrics.clicks,
            metrics.cost_micros,
            metrics.conversions,
            metrics.conversions_value,
            metrics.ctr,
            metrics.average_cpc
        FROM campaign
        WHERE segments.date BETWEEN '{start_date}' AND '{end_date}'
            AND campaign.status != 'REMOVED'
            AND metrics.impressions > 0
        ORDER BY segments.month ASC, campaign.name ASC
    """
    rows = []
    response = ga_service.search(customer_id=customer_id, query=query)
    for row in response:
        month_str = row.segments.month
        rows.append({
            'monat': month_str,
            'campaign': row.campaign.name,
            'impressions': row.metrics.impressions,
            'clicks': row.metrics.clicks,
            'cost': row.metrics.cost_micros / 1_000_000,
            'conversions': row.metrics.conversions,
            'conv_value': row.metrics.conversions_value,
            'ctr': row.metrics.ctr,
            'avg_cpc': row.metrics.average_cpc / 1_000_000,
        })
    return rows


def fetch_ga4_monthly_overview(ga4_client, prop, start_date, end_date):
    """Fetch GA4 data broken down by year-month for historical view."""
    date_range = DateRange(start_date=start_date, end_date=end_date)
    request = RunReportRequest(
        property=prop,
        date_ranges=[date_range],
        dimensions=[Dimension(name='yearMonth')],
        metrics=[
            Metric(name='sessions'),
            Metric(name='totalUsers'),
            Metric(name='newUsers'),
            Metric(name='screenPageViews'),
            Metric(name='averageSessionDuration'),
            Metric(name='bounceRate'),
            Metric(name='conversions'),
        ],
        limit=100,
    )
    response = ga4_client.run_report(request)
    headers = ['yearMonth'] + [h.name for h in response.metric_headers]
    rows = []
    for row in response.rows:
        values = [row.dimension_values[0].value] + [m.value for m in row.metric_values]
        rows.append(dict(zip(headers, values)))
    rows.sort(key=lambda r: r.get('yearMonth', ''))
    return headers, rows


def fetch_ads_ad_performance(ads_client, customer_id, start_date, end_date):
    ga_service = ads_client.get_service("GoogleAdsService")
    query = f"""
        SELECT
            ad_group_ad.ad.responsive_search_ad.headlines,
            campaign.name,
            ad_group.name,
            metrics.impressions,
            metrics.clicks,
            metrics.cost_micros,
            metrics.conversions,
            metrics.ctr,
            metrics.average_cpc
        FROM ad_group_ad
        WHERE segments.date BETWEEN '{start_date}' AND '{end_date}'
            AND ad_group_ad.status != 'REMOVED'
        ORDER BY metrics.impressions DESC
        LIMIT 20
    """
    rows = []
    response = ga_service.search(customer_id=customer_id, query=query)
    for row in response:
        headlines = []
        if row.ad_group_ad.ad.responsive_search_ad.headlines:
            headlines = [h.text for h in row.ad_group_ad.ad.responsive_search_ad.headlines[:3]]
        headline_text = ' | '.join(headlines) if headlines else row.ad_group.name

        rows.append({
            'ad': headline_text[:80],
            'campaign': row.campaign.name,
            'impressions': row.metrics.impressions,
            'clicks': row.metrics.clicks,
            'cost': row.metrics.cost_micros / 1_000_000,
            'conversions': row.metrics.conversions,
            'ctr': row.metrics.ctr,
            'avg_cpc': row.metrics.average_cpc / 1_000_000,
        })
    return rows


# --- Data Formatting ---

def response_to_rows(response):
    headers = [h.name for h in response.dimension_headers] + \
              [h.name for h in response.metric_headers]
    rows = []
    for row in response.rows:
        values = [d.value for d in row.dimension_values] + \
                 [m.value for m in row.metric_values]
        rows.append(dict(zip(headers, values)))
    return headers, rows

def fmt_number(val):
    try:
        f = float(val)
        if f == int(f):
            return f"{int(f):,}".replace(',', '.')
        return f"{f:.2f}".replace('.', ',')
    except (ValueError, TypeError):
        return val

def fmt_currency(val):
    try:
        f = float(val)
        return f"{f:,.2f} \u20ac".replace(',', 'X').replace('.', ',').replace('X', '.')
    except (ValueError, TypeError):
        return val

def fmt_duration(seconds_str):
    try:
        s = float(seconds_str)
        m, sec = divmod(int(s), 60)
        return f"{m}:{sec:02d}"
    except (ValueError, TypeError):
        return seconds_str

def fmt_percent(val):
    try:
        f = float(val)
        if f < 1:
            return f"{f*100:.1f}%".replace('.', ',')
        return f"{f:.1f}%".replace('.', ',')
    except (ValueError, TypeError):
        return val

def fmt_date(val):
    try:
        d = datetime.strptime(val, '%Y%m%d')
        return d.strftime('%d.%m.%Y')
    except (ValueError, TypeError):
        return val


# --- HTML Generation ---

def generate_html_table(headers, rows, formatters=None):
    label_map = {
        'date': 'Datum',
        'sessions': 'Sitzungen',
        'totalUsers': 'Nutzer',
        'newUsers': 'Neue Nutzer',
        'screenPageViews': 'Seitenaufrufe',
        'averageSessionDuration': 'Avg. Dauer',
        'bounceRate': 'Absprungrate',
        'conversions': 'Conversions',
        'sessionDefaultChannelGroup': 'Kanal',
        'landingPagePlusQueryString': 'Landingpage',
        'deviceCategory': 'Geraet',
        'country': 'Land',
        'sessionSourceMedium': 'Quelle/Medium',
        # Google Ads
        'campaign': 'Kampagne',
        'status': 'Status',
        'impressions': 'Impressionen',
        'clicks': 'Klicks',
        'cost': 'Kosten',
        'conv_value': 'Conv. Wert',
        'ctr': 'CTR',
        'avg_cpc': 'Avg. CPC',
        'cost_per_conv': 'Kosten/Conv.',
        'keyword': 'Keyword',
        'match_type': 'Match-Typ',
        'impression_share': 'Impr. Share',
        'search_term': 'Suchbegriff',
        'ad': 'Anzeige',
        'monat': 'Monat',
        'aktive_kampagnen': 'Aktive Kampagnen',
        'yearMonth': 'Monat',
    }

    duration_cols = {'averageSessionDuration'}
    percent_cols = {'bounceRate', 'ctr', 'impression_share'}
    date_cols = {'date'}
    number_cols = {'sessions', 'totalUsers', 'newUsers', 'screenPageViews',
                   'conversions', 'impressions', 'clicks'}
    currency_cols = {'cost', 'avg_cpc', 'cost_per_conv', 'conv_value'}

    html = '<table>\n<thead><tr>'
    for h in headers:
        label = label_map.get(h, h)
        html += f'<th>{label}</th>'
    html += '</tr></thead>\n<tbody>\n'

    for row in rows:
        html += '<tr>'
        for h in headers:
            val = row.get(h, '')
            if h in date_cols:
                val = fmt_date(val)
            elif h in duration_cols:
                val = fmt_duration(val)
            elif h in percent_cols:
                val = fmt_percent(val)
            elif h in currency_cols:
                val = fmt_currency(val)
            elif h in number_cols:
                val = fmt_number(val)
            html += f'<td>{val}</td>'
        html += '</tr>\n'

    html += '</tbody>\n</table>'
    return html


def generate_ads_table(rows, columns):
    """Generate HTML table from Google Ads dict rows with specified columns."""
    return generate_html_table(columns, rows)


def generate_summary_stats(rows, label="Zeitraum"):
    if not rows:
        return '<p>Keine Daten verfuegbar.</p>'

    total_sessions = sum(int(r.get('sessions', 0)) for r in rows)
    total_users = sum(int(r.get('totalUsers', 0)) for r in rows)
    total_new = sum(int(r.get('newUsers', 0)) for r in rows)
    total_conversions = sum(int(r.get('conversions', 0)) for r in rows)
    total_pageviews = sum(int(r.get('screenPageViews', 0)) for r in rows)

    avg_bounce = 0
    bounce_vals = [float(r.get('bounceRate', 0)) for r in rows if r.get('bounceRate')]
    if bounce_vals:
        avg_bounce = sum(bounce_vals) / len(bounce_vals)

    avg_duration = 0
    dur_vals = [float(r.get('averageSessionDuration', 0)) for r in rows if r.get('averageSessionDuration')]
    if dur_vals:
        avg_duration = sum(dur_vals) / len(dur_vals)

    conv_rate = (total_conversions / total_sessions * 100) if total_sessions > 0 else 0

    return f"""
    <div class="summary-grid">
        <div class="stat-card">
            <div class="stat-value">{fmt_number(str(total_sessions))}</div>
            <div class="stat-label">Sitzungen</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">{fmt_number(str(total_users))}</div>
            <div class="stat-label">Nutzer</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">{fmt_number(str(total_new))}</div>
            <div class="stat-label">Neue Nutzer</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">{fmt_number(str(total_pageviews))}</div>
            <div class="stat-label">Seitenaufrufe</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">{fmt_number(str(total_conversions))}</div>
            <div class="stat-label">Conversions</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">{conv_rate:.1f}%</div>
            <div class="stat-label">Conv. Rate</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">{fmt_duration(str(avg_duration))}</div>
            <div class="stat-label">Avg. Dauer</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">{fmt_percent(str(avg_bounce))}</div>
            <div class="stat-label">Absprungrate</div>
        </div>
    </div>
    """


def generate_ads_summary_stats(campaign_rows):
    if not campaign_rows:
        return '<p>Keine Google Ads Daten verfuegbar.</p>'

    total_impressions = sum(r.get('impressions', 0) for r in campaign_rows)
    total_clicks = sum(r.get('clicks', 0) for r in campaign_rows)
    total_cost = sum(r.get('cost', 0) for r in campaign_rows)
    total_conversions = sum(r.get('conversions', 0) for r in campaign_rows)
    total_conv_value = sum(r.get('conv_value', 0) for r in campaign_rows)
    avg_ctr = (total_clicks / total_impressions * 100) if total_impressions > 0 else 0
    avg_cpc = (total_cost / total_clicks) if total_clicks > 0 else 0
    cost_per_conv = (total_cost / total_conversions) if total_conversions > 0 else 0
    roas = (total_conv_value / total_cost) if total_cost > 0 else 0

    return f"""
    <div class="summary-grid">
        <div class="stat-card">
            <div class="stat-value">{fmt_number(str(total_impressions))}</div>
            <div class="stat-label">Impressionen</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">{fmt_number(str(total_clicks))}</div>
            <div class="stat-label">Klicks</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">{avg_ctr:.1f}%</div>
            <div class="stat-label">CTR</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">{fmt_currency(avg_cpc)}</div>
            <div class="stat-label">Avg. CPC</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">{fmt_currency(total_cost)}</div>
            <div class="stat-label">Gesamtkosten</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">{fmt_number(str(int(total_conversions)))}</div>
            <div class="stat-label">Conversions</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">{fmt_currency(cost_per_conv)}</div>
            <div class="stat-label">Kosten/Conv.</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">{roas:.2f}x</div>
            <div class="stat-label">ROAS</div>
        </div>
    </div>
    """


def build_html_report(title, date_label, sections, generated_at=None):
    if not generated_at:
        generated_at = datetime.now().strftime('%d.%m.%Y %H:%M')

    sections_html = ''
    for section in sections:
        sections_html += f"""
        <section>
            <h2>{section['title']}</h2>
            {section['content']}
        </section>
        """

    return f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            color: #1a1a2e;
            background: #f8f9fa;
            padding: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }}
        header {{
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            color: white;
            padding: 2rem;
            border-radius: 12px;
            margin-bottom: 2rem;
        }}
        header h1 {{ font-size: 1.8rem; margin-bottom: 0.5rem; }}
        header .meta {{ opacity: 0.8; font-size: 0.9rem; }}
        .section-divider {{
            background: linear-gradient(135deg, #2d3748 0%, #4a5568 100%);
            color: white;
            padding: 1rem 2rem;
            border-radius: 8px;
            margin: 2rem 0 1.5rem 0;
            font-size: 1.1rem;
            font-weight: 600;
        }}
        .summary-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
            gap: 1rem;
            margin: 1.5rem 0;
        }}
        .stat-card {{
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 1.2rem;
            text-align: center;
        }}
        .stat-value {{
            font-size: 1.6rem;
            font-weight: 700;
            color: #1a1a2e;
        }}
        .stat-label {{
            font-size: 0.8rem;
            color: #64748b;
            margin-top: 0.3rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}
        section {{
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 1.5rem 2rem;
            margin-bottom: 1.5rem;
        }}
        section h2 {{
            font-size: 1.2rem;
            color: #1a1a2e;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #f1f5f9;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.85rem;
        }}
        th {{
            background: #f8fafc;
            text-align: left;
            padding: 0.7rem 0.8rem;
            font-weight: 600;
            color: #475569;
            border-bottom: 2px solid #e2e8f0;
            white-space: nowrap;
        }}
        td {{
            padding: 0.6rem 0.8rem;
            border-bottom: 1px solid #f1f5f9;
        }}
        tr:hover {{ background: #f8fafc; }}
        .executive-summary {{
            line-height: 1.6;
            color: #334155;
        }}
        .executive-summary p {{ margin-bottom: 0.8rem; }}
        .executive-summary ul {{ margin: 0.5rem 0 1rem 1.5rem; }}
        .executive-summary li {{ margin-bottom: 0.4rem; }}
        .next-steps {{
            line-height: 1.6;
            color: #334155;
        }}
        .next-steps ol {{ margin: 0.5rem 0 0 1.5rem; }}
        .next-steps li {{ margin-bottom: 0.6rem; }}
        .next-steps li strong {{ color: #1a1a2e; }}
        footer {{
            text-align: center;
            color: #94a3b8;
            font-size: 0.8rem;
            margin-top: 2rem;
            padding: 1rem;
        }}
        @media print {{
            body {{ padding: 1rem; background: white; }}
            header {{ break-after: avoid; }}
            section {{ break-inside: avoid; }}
        }}
        @media (max-width: 600px) {{
            body {{ padding: 1rem; }}
            .summary-grid {{ grid-template-columns: repeat(2, 1fr); }}
        }}
    </style>
</head>
<body>
    <header>
        <h1>{title}</h1>
        <div class="meta">{date_label} | Erstellt: {generated_at}</div>
    </header>

    {sections_html}

    <footer>
        Flowbeaver Marketing Report | Automatisch generiert via GA4 + Google Ads API
    </footer>
</body>
</html>"""


# --- Report Types ---

def generate_executive_summary(overview_rows, source_rows, landing_rows, ads_campaigns=None):
    total_sessions = sum(int(r.get('sessions', 0)) for r in overview_rows)
    total_users = sum(int(r.get('totalUsers', 0)) for r in overview_rows)
    total_conversions = sum(int(r.get('conversions', 0)) for r in overview_rows)
    conv_rate = (total_conversions / total_sessions * 100) if total_sessions > 0 else 0

    top_source = source_rows[0] if source_rows else {}
    top_source_name = top_source.get('sessionDefaultChannelGroup', 'N/A')
    top_source_sessions = int(top_source.get('sessions', 0))

    top_lp = landing_rows[0] if landing_rows else {}
    top_lp_name = top_lp.get('landingPagePlusQueryString', 'N/A')

    ads_html = ''
    if ads_campaigns:
        total_ads_cost = sum(r.get('cost', 0) for r in ads_campaigns)
        total_ads_clicks = sum(r.get('clicks', 0) for r in ads_campaigns)
        total_ads_conv = sum(r.get('conversions', 0) for r in ads_campaigns)
        total_ads_impressions = sum(r.get('impressions', 0) for r in ads_campaigns)
        ads_ctr = (total_ads_clicks / total_ads_impressions * 100) if total_ads_impressions > 0 else 0
        ads_html = f"""
        <p><strong>Google Ads:</strong> {fmt_number(str(total_ads_impressions))} Impressionen,
        {fmt_number(str(total_ads_clicks))} Klicks (CTR: {ads_ctr:.1f}%),
        {fmt_currency(total_ads_cost)} Gesamtkosten,
        {fmt_number(str(int(total_ads_conv)))} Conversions.</p>
        """

    return f"""
    <div class="executive-summary">
        <p><strong>Website (GA4):</strong> Im Berichtszeitraum wurden <strong>{fmt_number(str(total_sessions))} Sitzungen</strong>
        von <strong>{fmt_number(str(total_users))} Nutzern</strong> verzeichnet.
        Es gab <strong>{fmt_number(str(total_conversions))} Conversions</strong>
        (Conversion Rate: <strong>{conv_rate:.1f}%</strong>).</p>
        {ads_html}
        <ul>
            <li><strong>Staerkster Kanal:</strong> {top_source_name} mit {fmt_number(str(top_source_sessions))} Sitzungen</li>
            <li><strong>Top Landingpage:</strong> {top_lp_name}</li>
        </ul>
    </div>
    """

def generate_next_steps(overview_rows, source_rows, landing_rows, ads_campaigns=None, ads_keywords=None):
    total_conversions = sum(int(r.get('conversions', 0)) for r in overview_rows)
    total_sessions = sum(int(r.get('sessions', 0)) for r in overview_rows)

    steps = []

    # Check conversion rate
    conv_rate = (total_conversions / total_sessions * 100) if total_sessions > 0 else 0
    if conv_rate < 2:
        steps.append("<strong>Conversion-Optimierung:</strong> Die Conversion Rate liegt unter 2%. Landingpages auf CTA-Platzierung und Formularlaenge pruefen.")

    # Check bounce rates by source
    high_bounce = [r for r in source_rows if float(r.get('bounceRate', 0)) > 0.7]
    if high_bounce:
        names = ', '.join(r.get('sessionDefaultChannelGroup', '') for r in high_bounce[:3])
        steps.append(f"<strong>Absprungraten senken:</strong> Hohe Absprungraten bei: {names}. Landing-Page-Relevanz und Ladezeiten pruefen.")

    # Check if organic is underperforming
    organic = [r for r in source_rows if 'organic' in r.get('sessionDefaultChannelGroup', '').lower()]
    paid = [r for r in source_rows if 'paid' in r.get('sessionDefaultChannelGroup', '').lower()]
    if organic and paid:
        org_sessions = int(organic[0].get('sessions', 0))
        paid_sessions = int(paid[0].get('sessions', 0))
        if org_sessions < paid_sessions:
            steps.append("<strong>SEO staerken:</strong> Organic liegt hinter Paid Search. Content-Produktion und interne Verlinkung intensivieren.")

    # Check landing page diversity
    if len(landing_rows) <= 3:
        steps.append("<strong>Landingpage-Portfolio erweitern:</strong> Traffic konzentriert sich auf wenige Seiten. Weitere themenspezifische Landingpages erstellen.")

    if total_conversions == 0:
        steps.append("<strong>Conversion-Tracking pruefen:</strong> Keine Conversions im Zeitraum. GA4-Events und Conversion-Markierungen verifizieren.")

    # Google Ads specific recommendations
    if ads_campaigns:
        total_cost = sum(r.get('cost', 0) for r in ads_campaigns)
        total_ads_conv = sum(r.get('conversions', 0) for r in ads_campaigns)
        if total_cost > 0 and total_ads_conv == 0:
            steps.append(f"<strong>Ads Budget pruefen:</strong> {fmt_currency(total_cost)} ausgegeben ohne Conversions. Keywords und Landingpages auf Relevanz pruefen.")

        # Check for low CTR campaigns
        low_ctr = [r for r in ads_campaigns if r.get('ctr', 0) < 0.02 and r.get('impressions', 0) > 100]
        if low_ctr:
            names = ', '.join(r.get('campaign', '') for r in low_ctr[:2])
            steps.append(f"<strong>Anzeigentexte optimieren:</strong> Niedrige CTR bei: {names}. Headlines und Descriptions testen.")

        # Check for expensive CPCs
        high_cpc = [r for r in ads_campaigns if r.get('avg_cpc', 0) > 10]
        if high_cpc:
            steps.append("<strong>CPC-Optimierung:</strong> Durchschnittliche CPCs ueber 10 EUR. Long-Tail-Keywords und Negative Keywords pruefen.")

    if ads_keywords:
        # Check for low impression share
        low_share = [r for r in ads_keywords if 0 < r.get('impression_share', 0) < 0.3 and r.get('conversions', 0) > 0]
        if low_share:
            kws = ', '.join(r.get('keyword', '') for r in low_share[:3])
            steps.append(f"<strong>Budget/Gebote erhoehen:</strong> Konvertierende Keywords mit niedrigem Impression Share: {kws}")

    if not steps:
        steps.append("<strong>Kurs halten:</strong> Die Metriken entwickeln sich positiv. Aktuelle Strategie beibehalten und weiter optimieren.")

    steps_html = '\n'.join(f'<li>{s}</li>' for s in steps)
    return f'<div class="next-steps"><ol>{steps_html}</ol></div>'


def create_report(ga4_client, prop, report_type, ads_client=None, ads_customer_id=None):
    today = datetime.now()

    if report_type == 'weekly':
        start = (today - timedelta(days=7)).strftime('%Y-%m-%d')
        end = (today - timedelta(days=1)).strftime('%Y-%m-%d')
        title = f"Woechentlicher Marketing-Report"
        date_label = f"{fmt_date(start.replace('-',''))} - {fmt_date(end.replace('-',''))}"
        filename = f"weekly-{today.strftime('%Y-%m-%d')}.html"
        out_dir = REPORTS_DIR / 'weekly'

    elif report_type == 'monthly':
        first_of_month = today.replace(day=1)
        last_month_end = first_of_month - timedelta(days=1)
        last_month_start = last_month_end.replace(day=1)
        start = last_month_start.strftime('%Y-%m-%d')
        end = last_month_end.strftime('%Y-%m-%d')
        title = f"Monatlicher Marketing-Report \u2014 {last_month_start.strftime('%B %Y')}"
        date_label = f"{fmt_date(start.replace('-',''))} - {fmt_date(end.replace('-',''))}"
        filename = f"monthly-{last_month_start.strftime('%Y-%m')}.html"
        out_dir = REPORTS_DIR / 'monthly'

    elif report_type == 'historical':
        start = '2024-01-01'
        end = (today - timedelta(days=1)).strftime('%Y-%m-%d')
        title = "Historischer Marketing-Gesamtreport"
        date_label = f"{fmt_date(start.replace('-',''))} - {fmt_date(end.replace('-',''))}"
        filename = f"historical-{today.strftime('%Y-%m-%d')}.html"
        out_dir = REPORTS_DIR / 'historical'

    else:
        print(f"Unbekannter Report-Typ: {report_type}")
        return

    date_range = DateRange(start_date=start, end_date=end)

    # --- GA4 Data ---
    print(f"  [GA4] Lade Traffic-Uebersicht...")
    overview_resp = fetch_traffic_overview(ga4_client, prop, date_range)
    _, overview_rows = response_to_rows(overview_resp)

    print(f"  [GA4] Lade Traffic-Quellen...")
    source_resp = fetch_traffic_sources(ga4_client, prop, date_range)
    source_headers, source_rows = response_to_rows(source_resp)

    print(f"  [GA4] Lade Landingpages...")
    lp_resp = fetch_landing_pages(ga4_client, prop, date_range)
    lp_headers, lp_rows = response_to_rows(lp_resp)

    print(f"  [GA4] Lade Geraete...")
    device_resp = fetch_devices(ga4_client, prop, date_range)
    device_headers, device_rows = response_to_rows(device_resp)

    print(f"  [GA4] Lade Geo-Daten...")
    geo_resp = fetch_geo(ga4_client, prop, date_range)
    geo_headers, geo_rows = response_to_rows(geo_resp)

    print(f"  [GA4] Lade Conversions nach Quelle...")
    conv_resp = fetch_conversions_by_source(ga4_client, prop, date_range)
    conv_headers, conv_rows = response_to_rows(conv_resp)

    # --- Google Ads Data ---
    ads_campaigns = []
    ads_keywords = []
    ads_search_terms = []
    ads_ads = []

    if ads_client and ads_customer_id:
        try:
            print(f"  [Ads] Lade Kampagnen-Performance...")
            ads_campaigns = fetch_ads_campaign_performance(ads_client, ads_customer_id, start, end)

            print(f"  [Ads] Lade Keyword-Performance...")
            ads_keywords = fetch_ads_keyword_performance(ads_client, ads_customer_id, start, end)

            print(f"  [Ads] Lade Suchbegriffe...")
            ads_search_terms = fetch_ads_search_terms(ads_client, ads_customer_id, start, end)

            print(f"  [Ads] Lade Anzeigen-Performance...")
            ads_ads = fetch_ads_ad_performance(ads_client, ads_customer_id, start, end)
        except Exception as e:
            print(f"  [Ads] Fehler beim Laden: {e}")
            print(f"  [Ads] Report wird ohne Google Ads Daten erstellt.")

    # --- Historical: monthly breakdown data ---
    ga4_monthly_headers = []
    ga4_monthly_rows = []
    ads_monthly_rows = []

    if report_type == 'historical':
        print(f"  [GA4] Lade monatliche Uebersicht...")
        ga4_monthly_headers, ga4_monthly_rows = fetch_ga4_monthly_overview(ga4_client, prop, start, end)

        if ads_client and ads_customer_id:
            try:
                print(f"  [Ads] Lade Kampagnen nach Monat...")
                ads_monthly_rows = fetch_ads_campaign_by_month(ads_client, ads_customer_id, start, end)
            except Exception as e:
                print(f"  [Ads] Monatsdaten nicht verfuegbar: {e}")

    # Build sections
    sections = [
        {
            'title': 'Executive Summary',
            'content': generate_executive_summary(overview_rows, source_rows, lp_rows, ads_campaigns),
        },
    ]

    if report_type == 'historical' and ga4_monthly_rows:
        # --- Historical: monthly GA4 timeline ---
        monthly_label_map = {'yearMonth': 'Monat', 'sessions': 'Sitzungen', 'totalUsers': 'Nutzer',
                             'newUsers': 'Neue Nutzer', 'screenPageViews': 'Seitenaufrufe',
                             'averageSessionDuration': 'Avg. Dauer', 'bounceRate': 'Absprungrate',
                             'conversions': 'Conversions'}
        # Format yearMonth to readable
        for row in ga4_monthly_rows:
            ym = row.get('yearMonth', '')
            if len(ym) == 6:
                row['yearMonth'] = f"{ym[4:6]}/{ym[:4]}"

        sections.append({
            'title': 'Website-Traffic im Zeitverlauf (monatlich)',
            'content': '<div class="section-divider">Google Analytics — Monatsverlauf</div>'
                       + generate_html_table(ga4_monthly_headers, ga4_monthly_rows),
        })

        # --- Historical: monthly Ads timeline ---
        if ads_monthly_rows:
            # Group by month, aggregate
            from collections import OrderedDict
            months = OrderedDict()
            for row in ads_monthly_rows:
                m = row['monat']
                if m not in months:
                    months[m] = {'monat': m, 'campaigns': set(), 'impressions': 0, 'clicks': 0,
                                 'cost': 0, 'conversions': 0, 'conv_value': 0}
                months[m]['campaigns'].add(row['campaign'])
                months[m]['impressions'] += row['impressions']
                months[m]['clicks'] += row['clicks']
                months[m]['cost'] += row['cost']
                months[m]['conversions'] += row['conversions']
                months[m]['conv_value'] += row['conv_value']

            monthly_summary = []
            for m, d in months.items():
                # Format month
                try:
                    dt = datetime.strptime(m, '%Y-%m-%d')
                    month_label = dt.strftime('%m/%Y')
                except ValueError:
                    month_label = m
                ctr = (d['clicks'] / d['impressions'] * 100) if d['impressions'] > 0 else 0
                avg_cpc = (d['cost'] / d['clicks']) if d['clicks'] > 0 else 0
                monthly_summary.append({
                    'monat': month_label,
                    'aktive_kampagnen': ', '.join(sorted(d['campaigns'])),
                    'impressions': d['impressions'],
                    'clicks': d['clicks'],
                    'ctr': ctr,
                    'avg_cpc': avg_cpc,
                    'cost': d['cost'],
                    'conversions': int(d['conversions']),
                })

            sections.append({
                'title': 'Google Ads im Zeitverlauf (monatlich)',
                'content': '<div class="section-divider">Google Ads — Monatsverlauf</div>'
                           + generate_ads_table(monthly_summary,
                    ['monat', 'aktive_kampagnen', 'impressions', 'clicks', 'ctr', 'avg_cpc', 'cost', 'conversions']),
            })

            # Per-campaign timeline: show each campaign with its active months
            campaign_months = OrderedDict()
            for row in ads_monthly_rows:
                c = row['campaign']
                if c not in campaign_months:
                    campaign_months[c] = []
                try:
                    dt = datetime.strptime(row['monat'], '%Y-%m-%d')
                    month_label = dt.strftime('%m/%Y')
                except ValueError:
                    month_label = row['monat']
                campaign_months[c].append({
                    'monat': month_label,
                    'impressions': row['impressions'],
                    'clicks': row['clicks'],
                    'ctr': row['ctr'],
                    'avg_cpc': row['avg_cpc'],
                    'cost': row['cost'],
                    'conversions': int(row['conversions']),
                })

            for campaign_name, c_rows in campaign_months.items():
                if sum(r['impressions'] for r in c_rows) > 0:
                    sections.append({
                        'title': f'Kampagne: {campaign_name}',
                        'content': generate_ads_table(c_rows,
                            ['monat', 'impressions', 'clicks', 'ctr', 'avg_cpc', 'cost', 'conversions']),
                    })

    # GA4 sections (aggregated)
    sections.append({
        'title': 'Website-Analytics Gesamt (GA4)',
        'content': '<div class="section-divider">Google Analytics — Gesamtzeitraum</div>' + generate_summary_stats(overview_rows),
    })
    sections.append({
        'title': 'Traffic nach Kanal',
        'content': generate_html_table(source_headers, source_rows),
    })
    sections.append({
        'title': 'Top Landingpages',
        'content': generate_html_table(lp_headers, lp_rows),
    })
    sections.append({
        'title': 'Conversions nach Quelle',
        'content': generate_html_table(conv_headers, conv_rows),
    })
    sections.append({
        'title': 'Geraete',
        'content': generate_html_table(device_headers, device_rows),
    })
    sections.append({
        'title': 'Laender',
        'content': generate_html_table(geo_headers, geo_rows),
    })

    # Google Ads sections (aggregated)
    if ads_campaigns:
        sections.append({
            'title': 'Google Ads Gesamt',
            'content': '<div class="section-divider">Google Ads — Gesamtzeitraum</div>' + generate_ads_summary_stats(ads_campaigns),
        })
        sections.append({
            'title': 'Kampagnen-Performance (gesamt)',
            'content': generate_ads_table(ads_campaigns,
                ['campaign', 'status', 'impressions', 'clicks', 'ctr', 'avg_cpc', 'cost', 'conversions', 'cost_per_conv']),
        })

    if ads_keywords:
        sections.append({
            'title': 'Keyword-Performance (Top 30)',
            'content': generate_ads_table(ads_keywords,
                ['keyword', 'match_type', 'campaign', 'impressions', 'clicks', 'ctr', 'avg_cpc', 'cost', 'conversions', 'impression_share']),
        })

    if ads_search_terms:
        sections.append({
            'title': 'Suchbegriffe (Top 30)',
            'content': generate_ads_table(ads_search_terms,
                ['search_term', 'campaign', 'impressions', 'clicks', 'ctr', 'cost', 'conversions']),
        })

    if ads_ads:
        sections.append({
            'title': 'Anzeigen-Performance',
            'content': generate_ads_table(ads_ads,
                ['ad', 'campaign', 'impressions', 'clicks', 'ctr', 'avg_cpc', 'cost', 'conversions']),
        })

    # Next steps
    sections.append({
        'title': 'Empfohlene naechste Schritte',
        'content': generate_next_steps(overview_rows, source_rows, lp_rows, ads_campaigns, ads_keywords),
    })

    html = build_html_report(title, date_label, sections)

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / filename
    out_path.write_text(html, encoding='utf-8')
    print(f"  Report gespeichert: {out_path}")
    return out_path


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/ga4_report.py [weekly|monthly|historical|all]")
        sys.exit(1)

    report_type = sys.argv[1].lower()
    env = load_env()

    if not env.get('GOOGLE_REFRESH_TOKEN'):
        print("Fehler: Kein GOOGLE_REFRESH_TOKEN in .env.")
        print("Bitte zuerst ausfuehren: python3 scripts/google_auth.py")
        sys.exit(1)

    ga4_client = get_ga4_client(env)
    prop = get_property_id(env)

    # Google Ads (optional)
    ads_client = None
    ads_customer_id = None
    if env.get('GOOGLE_ADS_DEVELOPER_TOKEN') and env.get('GOOGLE_ADS_CUSTOMER_ID'):
        try:
            ads_client = get_ads_client(env)
            ads_customer_id = get_ads_customer_id(env)
            print("Google Ads API verbunden.")
        except Exception as e:
            print(f"Google Ads nicht verfuegbar: {e}")
            print("Report wird nur mit GA4-Daten erstellt.\n")

    if report_type == 'all':
        for rt in ['weekly', 'monthly', 'historical']:
            print(f"\n=== {rt.upper()} Report ===")
            create_report(ga4_client, prop, rt, ads_client, ads_customer_id)
    else:
        print(f"\n=== {report_type.upper()} Report ===")
        create_report(ga4_client, prop, report_type, ads_client, ads_customer_id)

    print("\nFertig!")


if __name__ == '__main__':
    main()
