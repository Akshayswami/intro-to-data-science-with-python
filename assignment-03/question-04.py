def answer_four():
    Top15 = answer_one()
    avgGDP = answer_three()
    country = avgGDP.keys()[5]
    ans = Top15.loc[country, '2015'] - Top15.loc[country, '2006']
    return ans
answer_four()
