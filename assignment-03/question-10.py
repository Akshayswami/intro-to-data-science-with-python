def answer_ten():
    Top15 = answer_one()
    median = np.median(Top15['% Renewable'])
    for i in range(len(Top15)):
        if Top15.iloc[i]['% Renewable'] >= median:
            Top15.set_value(Top15.iloc[i].name, 'HighRenew', 1)
        else:
            Top15.set_value(Top15.iloc[i].name, 'HighRenew', 0)
    Top15 = Top15['HighRenew']
    Top15 = Top15.sort(inplace=False)
    return Top15
answer_ten()
