def ratio(row):
    row['ratio'] = row['Self-citations'] / row['Citations']
    return row

def answer_seven():
    Top15 = answer_one()
    new = Top15.apply(ratio, axis=1)
    m = float(np.max(new['ratio']))
    country = new[new['ratio'] == m].iloc[0].name
    return country, m
answer_seven()
