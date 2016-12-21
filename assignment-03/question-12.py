def answer_twelve():
    Top15 = answer_one()
    for i in range(len(Top15)):
        country = Top15.iloc[i].name
        Top15.set_value(country, 'Continent', ContinentDict[country])
    Top15 = (Top15.reset_index(level=0)
                 .set_index(['Continent', 'Country']))
    Top15 = pd.cut(Top15['% Renewable'], 5)
    Top15 = (Top15.reset_index()
                .set_index(['Continent', '% Renewable']))
    Top15 = Top15.groupby(level=['Continent', '% Renewable']).size()
    return Top15
answer_twelve()
