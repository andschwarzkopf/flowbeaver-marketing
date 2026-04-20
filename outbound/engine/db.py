"""SQLite-Datenbank: Schema-Erstellung und CRUD-Funktionen."""

import sqlite3
from contextlib import contextmanager
from urllib.parse import urlparse

from .config import DB_PATH, KO_CRITERIA


def _normalize_domain(url: str) -> str:
    """Extrahiert und normalisiert Domain aus URL."""
    if not url:
        return ""
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    parsed = urlparse(url)
    domain = parsed.netloc.lower()
    if domain.startswith("www."):
        domain = domain[4:]
    return domain


@contextmanager
def get_db():
    """Context-Manager für DB-Verbindung."""
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init_db():
    """Erstellt alle Tabellen und seeded KO-Kriterien."""
    with get_db() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS kanzleien (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                website TEXT,
                domain TEXT UNIQUE,
                city TEXT,
                region TEXT,
                bundesland TEXT,
                source_first_found TEXT,
                linkedin_company TEXT,
                team_page_url TEXT,
                career_page_url TEXT,
                estimated_size INTEGER,
                contact_1_name TEXT,
                contact_1_role TEXT,
                contact_1_linkedin TEXT,
                contact_2_name TEXT,
                contact_2_role TEXT,
                notes TEXT,
                review_status TEXT DEFAULT 'pending'
                    CHECK(review_status IN ('pending','approved','rejected','needs_research')),
                review_notes TEXT,
                created_at TEXT DEFAULT (datetime('now')),
                updated_at TEXT DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS signals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                kanzlei_id INTEGER NOT NULL REFERENCES kanzleien(id),
                signal_type TEXT NOT NULL,
                observation TEXT,
                source_url TEXT,
                source_type TEXT,
                found_at TEXT DEFAULT (datetime('now')),
                outreach_relevant INTEGER DEFAULT 0,
                personalization_anchor TEXT
            );

            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                kanzlei_id INTEGER NOT NULL UNIQUE REFERENCES kanzleien(id),
                size_score INTEGER DEFAULT 0 CHECK(size_score BETWEEN 0 AND 2),
                fibu_score INTEGER DEFAULT 0 CHECK(fibu_score BETWEEN 0 AND 2),
                digital_score INTEGER DEFAULT 0 CHECK(digital_score BETWEEN 0 AND 2),
                datev_score INTEGER DEFAULT 0 CHECK(datev_score BETWEEN 0 AND 2),
                growth_score INTEGER DEFAULT 0 CHECK(growth_score BETWEEN 0 AND 2),
                recruiting_score INTEGER DEFAULT 0 CHECK(recruiting_score BETWEEN 0 AND 2),
                process_score INTEGER DEFAULT 0 CHECK(process_score BETWEEN 0 AND 2),
                tools_score INTEGER DEFAULT 0 CHECK(tools_score BETWEEN 0 AND 2),
                decision_maker_score INTEGER DEFAULT 0 CHECK(decision_maker_score BETWEEN 0 AND 2),
                trigger_score INTEGER DEFAULT 0 CHECK(trigger_score BETWEEN 0 AND 2),
                total INTEGER GENERATED ALWAYS AS (
                    size_score + fibu_score + digital_score + datev_score +
                    growth_score + recruiting_score + process_score + tools_score +
                    decision_maker_score + trigger_score
                ) STORED,
                tier TEXT GENERATED ALWAYS AS (
                    CASE
                        WHEN (size_score + fibu_score + digital_score + datev_score +
                              growth_score + recruiting_score + process_score + tools_score +
                              decision_maker_score + trigger_score) >= 16 THEN 'A'
                        WHEN (size_score + fibu_score + digital_score + datev_score +
                              growth_score + recruiting_score + process_score + tools_score +
                              decision_maker_score + trigger_score) >= 11 THEN 'B'
                        ELSE 'C'
                    END
                ) STORED,
                ko_hit INTEGER DEFAULT 0,
                ko_reason TEXT,
                summary TEXT,
                scored_by TEXT DEFAULT 'claude',
                scored_at TEXT DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS search_runs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                query TEXT NOT NULL,
                city TEXT,
                region TEXT,
                source TEXT,
                results_count INTEGER DEFAULT 0,
                new_kanzleien_count INTEGER DEFAULT 0,
                run_at TEXT DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS ko_criteria (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code TEXT UNIQUE NOT NULL,
                label_de TEXT NOT NULL,
                description TEXT
            );
        """)

        # KO-Kriterien seeden
        for code, label in KO_CRITERIA.items():
            conn.execute(
                "INSERT OR IGNORE INTO ko_criteria (code, label_de) VALUES (?, ?)",
                (code, label),
            )


# --- Kanzleien CRUD ---

def add_kanzlei(name: str, website: str, city: str = "", region: str = "",
                source: str = "brave_search", **kwargs) -> int | None:
    """Fügt Kanzlei hinzu. Gibt ID zurück oder None bei Duplikat."""
    domain = _normalize_domain(website)
    if not domain:
        return None

    with get_db() as conn:
        try:
            cur = conn.execute(
                """INSERT INTO kanzleien
                   (name, website, domain, city, region, source_first_found,
                    linkedin_company, team_page_url, career_page_url,
                    estimated_size, notes)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (name, website, domain, city, region, source,
                 kwargs.get("linkedin_company", ""),
                 kwargs.get("team_page_url", ""),
                 kwargs.get("career_page_url", ""),
                 kwargs.get("estimated_size"),
                 kwargs.get("notes", "")),
            )
            return cur.lastrowid
        except sqlite3.IntegrityError:
            # Domain existiert bereits
            return None


def get_kanzlei(kanzlei_id: int) -> dict | None:
    with get_db() as conn:
        row = conn.execute("SELECT * FROM kanzleien WHERE id = ?", (kanzlei_id,)).fetchone()
        return dict(row) if row else None


def get_kanzlei_by_domain(domain: str) -> dict | None:
    domain = _normalize_domain(domain) if "." in domain else domain
    with get_db() as conn:
        row = conn.execute("SELECT * FROM kanzleien WHERE domain = ?", (domain,)).fetchone()
        return dict(row) if row else None


def update_kanzlei(kanzlei_id: int, **kwargs):
    """Aktualisiert beliebige Felder einer Kanzlei."""
    if not kwargs:
        return
    allowed = {
        "name", "website", "city", "region", "bundesland",
        "linkedin_company", "team_page_url", "career_page_url",
        "estimated_size", "contact_1_name", "contact_1_role", "contact_1_linkedin",
        "contact_2_name", "contact_2_role", "notes", "review_status", "review_notes",
    }
    fields = {k: v for k, v in kwargs.items() if k in allowed}
    if not fields:
        return
    sets = ", ".join(f"{k} = ?" for k in fields)
    vals = list(fields.values()) + [kanzlei_id]
    with get_db() as conn:
        conn.execute(
            f"UPDATE kanzleien SET {sets}, updated_at = datetime('now') WHERE id = ?",
            vals,
        )


def set_review_status(kanzlei_id: int, status: str, notes: str = ""):
    with get_db() as conn:
        conn.execute(
            "UPDATE kanzleien SET review_status = ?, review_notes = ?, updated_at = datetime('now') WHERE id = ?",
            (status, notes, kanzlei_id),
        )


def get_pending_reviews(limit: int = 20) -> list[dict]:
    with get_db() as conn:
        rows = conn.execute(
            "SELECT * FROM kanzleien WHERE review_status = 'pending' ORDER BY created_at LIMIT ?",
            (limit,),
        ).fetchall()
        return [dict(r) for r in rows]


def search_kanzleien(review_status: str = None, tier: str = None,
                     city: str = None, region: str = None, limit: int = 100) -> list[dict]:
    """Flexible Suche mit optionalen Filtern."""
    query = """
        SELECT k.*, s.total, s.tier, s.ko_hit
        FROM kanzleien k
        LEFT JOIN scores s ON k.id = s.kanzlei_id
        WHERE 1=1
    """
    params = []
    if review_status:
        query += " AND k.review_status = ?"
        params.append(review_status)
    if tier:
        query += " AND s.tier = ?"
        params.append(tier)
    if city:
        query += " AND k.city = ?"
        params.append(city)
    if region:
        query += " AND k.region = ?"
        params.append(region)
    query += " ORDER BY s.total DESC NULLS LAST LIMIT ?"
    params.append(limit)
    with get_db() as conn:
        rows = conn.execute(query, params).fetchall()
        return [dict(r) for r in rows]


# --- Signals CRUD ---

def add_signal(kanzlei_id: int, signal_type: str, observation: str,
               source_url: str = "", source_type: str = "website",
               outreach_relevant: bool = False, personalization_anchor: str = "") -> int:
    with get_db() as conn:
        cur = conn.execute(
            """INSERT INTO signals
               (kanzlei_id, signal_type, observation, source_url, source_type,
                outreach_relevant, personalization_anchor)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (kanzlei_id, signal_type, observation, source_url, source_type,
             int(outreach_relevant), personalization_anchor),
        )
        return cur.lastrowid


def get_signals(kanzlei_id: int) -> list[dict]:
    with get_db() as conn:
        rows = conn.execute(
            "SELECT * FROM signals WHERE kanzlei_id = ? ORDER BY signal_type",
            (kanzlei_id,),
        ).fetchall()
        return [dict(r) for r in rows]


# --- Scores CRUD ---

def upsert_score(kanzlei_id: int, scores: dict, ko_hit: bool = False,
                 ko_reason: str = "", summary: str = "", scored_by: str = "claude"):
    """Insert oder Update Score für eine Kanzlei."""
    with get_db() as conn:
        conn.execute(
            """INSERT INTO scores
               (kanzlei_id, size_score, fibu_score, digital_score, datev_score,
                growth_score, recruiting_score, process_score, tools_score,
                decision_maker_score, trigger_score, ko_hit, ko_reason, summary, scored_by)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
               ON CONFLICT(kanzlei_id) DO UPDATE SET
                size_score=excluded.size_score, fibu_score=excluded.fibu_score,
                digital_score=excluded.digital_score, datev_score=excluded.datev_score,
                growth_score=excluded.growth_score, recruiting_score=excluded.recruiting_score,
                process_score=excluded.process_score, tools_score=excluded.tools_score,
                decision_maker_score=excluded.decision_maker_score,
                trigger_score=excluded.trigger_score,
                ko_hit=excluded.ko_hit, ko_reason=excluded.ko_reason,
                summary=excluded.summary, scored_by=excluded.scored_by,
                scored_at=datetime('now')""",
            (kanzlei_id,
             scores.get("size", 0), scores.get("fibu", 0), scores.get("digital", 0),
             scores.get("datev", 0), scores.get("growth", 0), scores.get("recruiting", 0),
             scores.get("process", 0), scores.get("tools", 0),
             scores.get("decision_maker", 0), scores.get("trigger", 0),
             int(ko_hit), ko_reason, summary, scored_by),
        )


def get_score(kanzlei_id: int) -> dict | None:
    with get_db() as conn:
        row = conn.execute("SELECT * FROM scores WHERE kanzlei_id = ?", (kanzlei_id,)).fetchone()
        return dict(row) if row else None


# --- Search Runs ---

def log_search_run(query: str, city: str = "", region: str = "",
                   source: str = "brave_search", results_count: int = 0,
                   new_count: int = 0) -> int:
    with get_db() as conn:
        cur = conn.execute(
            """INSERT INTO search_runs (query, city, region, source, results_count, new_kanzleien_count)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (query, city, region, source, results_count, new_count),
        )
        return cur.lastrowid


# --- Pipeline Stats ---

def get_pipeline_stats() -> dict:
    """Gibt Pipeline-Übersicht zurück."""
    with get_db() as conn:
        total = conn.execute("SELECT COUNT(*) FROM kanzleien").fetchone()[0]

        status_counts = {}
        for row in conn.execute(
            "SELECT review_status, COUNT(*) as cnt FROM kanzleien GROUP BY review_status"
        ).fetchall():
            status_counts[row["review_status"]] = row["cnt"]

        tier_counts = {}
        for row in conn.execute(
            "SELECT tier, COUNT(*) as cnt FROM scores GROUP BY tier"
        ).fetchall():
            tier_counts[row["tier"]] = row["cnt"]

        region_counts = {}
        for row in conn.execute(
            "SELECT region, COUNT(*) as cnt FROM kanzleien WHERE region != '' GROUP BY region"
        ).fetchall():
            region_counts[row["region"]] = row["cnt"]

        search_count = conn.execute("SELECT COUNT(*) FROM search_runs").fetchone()[0]

        return {
            "total": total,
            "by_status": status_counts,
            "by_tier": tier_counts,
            "by_region": region_counts,
            "search_runs": search_count,
        }


def get_approved_icps() -> list[dict]:
    """Alle approved Kanzleien mit Scores und besten Signalen."""
    with get_db() as conn:
        rows = conn.execute("""
            SELECT k.*, s.total, s.tier, s.summary,
                   s.size_score, s.fibu_score, s.digital_score, s.datev_score,
                   s.growth_score, s.recruiting_score, s.process_score, s.tools_score,
                   s.decision_maker_score, s.trigger_score
            FROM kanzleien k
            LEFT JOIN scores s ON k.id = s.kanzlei_id
            WHERE k.review_status = 'approved'
            ORDER BY s.total DESC
        """).fetchall()
        return [dict(r) for r in rows]
