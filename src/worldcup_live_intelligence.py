"""世界杯实时情报中心: core module."""

from dataclasses import dataclass
from typing import Any, Dict, List

@dataclass
class ProjectConfig:
    name: str = "worldcup-live-intelligence"
    title: str = "世界杯实时情报中心"
    primary_keywords: tuple = ('world cup 2026 live score', 'world cup fixtures', 'fifa world cup analytics', '2026 world cup predictor')

def normalize_match_record(record: Dict[str, Any]) -> Dict[str, Any]:
    """Normalize a football match record from API or offline JSON source."""
    return {
        "source_id": record.get("id") or record.get("match_id"),
        "utc_date": record.get("utcDate") or record.get("date"),
        "home_team": (record.get("homeTeam") or {}).get("name") if isinstance(record.get("homeTeam"), dict) else record.get("home_team"),
        "away_team": (record.get("awayTeam") or {}).get("name") if isinstance(record.get("awayTeam"), dict) else record.get("away_team"),
        "status": record.get("status") or record.get("stage"),
        "score": record.get("score"),
    }

def build_seo_keywords(extra: List[str] | None = None) -> List[str]:
    """Return de-duplicated SEO keyword set for project pages."""
    values = list(ProjectConfig.primary_keywords) + (extra or [])
    return list(dict.fromkeys(v.strip().lower() for v in values if v and v.strip()))
