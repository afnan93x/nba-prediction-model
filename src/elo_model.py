import pandas as pd

INITIAL = 1500
K = 20

def expected(r1,r2):
    return 1/(1+10**((r2-r1)/400))

def compute_elo(df):

    teams = pd.unique(df[['home_team','away_team']].values.ravel())
    elo = {t: INITIAL for t in teams}

    home_elos = []
    away_elos = []

    for _, row in df.iterrows():

        h = row.home_team
        a = row.away_team

        r_h = elo[h]
        r_a = elo[a]

        home_elos.append(r_h)
        away_elos.append(r_a)

        exp = expected(r_h,r_a)
        actual = row.home_win

        elo[h] += K*(actual-exp)
        elo[a] += K*((1-actual)-(1-exp))

    df["elo_diff"] = [h-a for h,a in zip(home_elos,away_elos)]

    return df
