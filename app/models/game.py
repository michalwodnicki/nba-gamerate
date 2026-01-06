from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Team:
    name: str
    win_pct: float          # 0.0–1.0
    pace_rank: int          # 1–30 (lower = faster)
    stars: int              # number of star players
    playoff_position: Optional[int]  # None if out of race


@dataclass(frozen=True)
class Game:
    home: Team
    away: Team
    is_division_rival: bool
    national_tv: bool