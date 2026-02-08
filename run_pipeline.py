from src.data_loader import load_season
from src.elo_model import compute_elo
from src.feature_builder import rolling_features
from src.train_model import train_model
from src.backtest import simulate

def run():

    games = load_season()

    df = compute_elo(df)
    df = rolling_features(df)

    model, df, split = train_model(df)
    history = simulate(df, split)

    print("Final Bankroll:", history[-1])

if __name__ == "__main__":
    run()