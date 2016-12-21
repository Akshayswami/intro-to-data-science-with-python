ContinentDict  = {'China':'Asia',
                  'United States':'North America',
                  'Japan':'Asia',
                  'United Kingdom':'Europe',
                  'Russian Federation':'Europe',
                  'Canada':'North America',
                  'Germany':'Europe',
                  'India':'Asia',
                  'France':'Europe',
                  'South Korea':'Asia',
                  'Italy':'Europe',
                  'Spain':'Europe',
                  'Iran':'Asia',
                  'Australia':'Australia',
                  'Brazil':'South America'}

def answer_eleven():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    for i in range(len(Top15)):
        country = Top15.iloc[i].name
        Top15.set_value(country, 'Continent', ContinentDict[country])
    Top15 = (Top15.reset_index(level=0)
                 .set_index(['Continent', 'Country']))
    Top15 = Top15.groupby(level=0)['PopEst'].agg({'size': np.size, 'sum': np.sum, 'mean': np.average, 'std': np.std})
    return Top15
answer_eleven()
