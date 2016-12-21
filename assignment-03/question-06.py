def answer_six():
    Top15 = answer_one()
    m = float(np.max(Top15['% Renewable']))
    country = Top15[Top15['% Renewable'] == m].iloc[0].name
    ans = country, m
    return ans
answer_six()
