from app.data.mock_games import MOCK_GAMES
from app.scoring.score_game import score_game


def main():
    print("Tonight's NBA Watchability Scores:\n")

    for game in MOCK_GAMES:
        score = score_game(game)
        print(f"{game.away.name} @ {game.home.name}: {score}/10")


if __name__ == "__main__":
    main()
