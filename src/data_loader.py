from nba_api.stats.endpoints import leaguegamefinder
import pandas as pd

def load_season(season="2025-26"):

    games = leaguegamefinder.LeagueGameFinder(
        season_nullable=season
    ).get_data_frames()[0]

    games = games[['GAME_ID','GAME_DATE','TEAM_NAME','MATCHUP','WL','PTS']]

    games['home'] = games['MATCHUP'].str.contains("vs.")
    games['win'] = (games['WL'] == 'W').astype(int)
    games['GAME_DATE'] = pd.to_datetime(games['GAME_DATE'])

    return games
