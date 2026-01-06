def clamp(value: float, min_value: float, max_value: float) -> float:
    return max(min_value, min(value, max_value))


def team_quality(avg_win_pct: float) -> float:
    return clamp(avg_win_pct * 2.5, 0.0, 2.5)


def competitiveness(win_pct_diff: float) -> float:
    return clamp((1 - win_pct_diff) * 3.0, 0.0, 3.0)


def star_power(total_stars: int) -> float:
    return clamp(total_stars * 0.5, 0.0, 2.0)


def pace(avg_pace_rank: int) -> float:
    return clamp((30 - avg_pace_rank) / 30, 0.0, 1.0)


def rivalry(is_division_rival: bool) -> float:
    return 0.75 if is_division_rival else 0.0


def playoff_implications(home_pos, away_pos) -> float:
    return 0.75 if home_pos and away_pos else 0.0
