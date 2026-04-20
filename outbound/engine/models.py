"""Dataclasses für die Outbound Engine."""

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Kanzlei:
    id: Optional[int] = None
    name: str = ""
    website: str = ""
    domain: str = ""
    city: str = ""
    region: str = ""
    bundesland: str = ""
    source_first_found: str = ""
    linkedin_company: str = ""
    team_page_url: str = ""
    career_page_url: str = ""
    estimated_size: Optional[int] = None
    contact_1_name: str = ""
    contact_1_role: str = ""
    contact_1_linkedin: str = ""
    contact_2_name: str = ""
    contact_2_role: str = ""
    notes: str = ""
    review_status: str = "pending"
    review_notes: str = ""
    created_at: str = ""
    updated_at: str = ""


@dataclass
class Signal:
    id: Optional[int] = None
    kanzlei_id: int = 0
    signal_type: str = ""  # Eine der 10 Dimensionen aus SIGNAL_KEYS
    observation: str = ""
    source_url: str = ""
    source_type: str = ""  # website, career, linkedin, job_posting, event, directory
    found_at: str = ""
    outreach_relevant: bool = False
    personalization_anchor: str = ""


@dataclass
class Score:
    id: Optional[int] = None
    kanzlei_id: int = 0
    size_score: int = 0
    fibu_score: int = 0
    digital_score: int = 0
    datev_score: int = 0
    growth_score: int = 0
    recruiting_score: int = 0
    process_score: int = 0
    tools_score: int = 0
    decision_maker_score: int = 0
    trigger_score: int = 0
    total: int = 0
    tier: str = "C"
    ko_hit: bool = False
    ko_reason: str = ""
    summary: str = ""
    scored_by: str = "claude"
    scored_at: str = ""

    @property
    def score_dict(self) -> dict:
        return {
            "size": self.size_score,
            "fibu": self.fibu_score,
            "digital": self.digital_score,
            "datev": self.datev_score,
            "growth": self.growth_score,
            "recruiting": self.recruiting_score,
            "process": self.process_score,
            "tools": self.tools_score,
            "decision_maker": self.decision_maker_score,
            "trigger": self.trigger_score,
        }


@dataclass
class SearchResult:
    """Rohes Ergebnis aus BraveSearch vor Verarbeitung."""
    title: str = ""
    url: str = ""
    domain: str = ""
    description: str = ""
    query: str = ""
    city: str = ""
