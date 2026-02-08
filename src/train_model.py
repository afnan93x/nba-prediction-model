from sklearn.linear_model import LogisticRegression

def train_model(df):

    features = ["elo_diff","home_last5","away_last5"]

    X = df[features]
    y = df["home_win"]

    split = int(len(df)*0.7)

    model = LogisticRegression()
    model.fit(X.iloc[:split], y.iloc[:split])

    df.loc[X.iloc[split:].index,"model_prob"] = \
        model.predict_proba(X.iloc[split:])[:,1]

    return model, df, split
