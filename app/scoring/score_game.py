from app.models.game import Game
from app.scoring import features


def score_game(game: Game) -> float:
    avg_win_pct = (game.home.win_pct + game.away.win_pct) / 2
    win_pct_diff = abs(game.home.win_pct - game.away.win_pct)
    total_stars = game.home.stars + game.away.stars
    avg_pace_rank = (game.home.pace_rank + game.away.pace_rank) // 2

    score = (
        features.team_quality(avg_win_pct)
        + features.competitiveness(win_pct_diff)
        + features.star_power(total_stars)
        + features.pace(avg_pace_rank)
        + features.rivalry(game.is_division_rival)
        + features.playoff_implications(
            game.home.playoff_position,
            game.away.playoff_position,
        )
    )

    return round(features.clamp(score, 1.0, 10.0), 1)
