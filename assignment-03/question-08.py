def answer_eight():
    Top15 = answer_one()
    new = Top15.apply(lambda x: x['Energy Supply'] / x['Energy Supply per Capita'], axis=1)
    new.sort(ascending=False)
    country = new.keys()[2]
    return country
answer_eight()
