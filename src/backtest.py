def simulate(df, split):

    bankroll = 1000
    history = []

    for _, row in df.iloc[split:].iterrows():

        prob = row.model_prob

        if prob > 0.55:
            stake = bankroll * 0.02

            if row.home_win:
                bankroll += stake
            else:
                bankroll -= stake

        history.append(bankroll)

    return history
