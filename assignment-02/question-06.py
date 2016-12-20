def answer_six():
    only_counties = census_df.where(census_df['SUMLEV'] == 50)
    only_counties = only_counties.dropna()
    columns_to_keep = ['STNAME', 'CTYNAME', 'CENSUS2010POP']
    only_counties = only_counties[columns_to_keep]
    only_counties = only_counties.set_index('STNAME')
    only_counties.sort_values('CENSUS2010POP', ascending=False, inplace=True)
    d = {}
    for i in range(len(only_counties)):
        state = only_counties.iloc[i].name
        try:
            if len(d[state]) < 3:
                d[state].append(only_counties.iloc[i]['CENSUS2010POP'])
        except KeyError:
            d[state] = []
            d[state].append(only_counties.iloc[i]['CENSUS2010POP'])
    for state in d:
        d[state] = sum(d[state])
    ans = []
    newdf = pd.DataFrame(d, index=range(0,len(d)))
    newdf = newdf.T[0]
    newdf = newdf.sort_values(ascending=False)
    for i in range(3):
        ans.append(newdf[newdf == newdf.iloc[i]].index[0])
    return ans
answer_six()
