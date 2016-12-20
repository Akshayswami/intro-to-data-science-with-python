def answer_seven():
    only_counties = census_df.where(census_df['SUMLEV'] == 50)
    only_counties = only_counties.dropna()
    columns_to_keep = ['CTYNAME', 'POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']
    only_counties = only_counties[columns_to_keep]
    only_counties = only_counties.set_index('CTYNAME')
    amax = 0
    ans = ""
    for i in range(len(only_counties)):
        popl = []
        popl.append(only_counties.iloc[i]['POPESTIMATE2010'])
        popl.append(only_counties.iloc[i]['POPESTIMATE2011'])
        popl.append(only_counties.iloc[i]['POPESTIMATE2012'])
        popl.append(only_counties.iloc[i]['POPESTIMATE2013'])
        popl.append(only_counties.iloc[i]['POPESTIMATE2014'])
        popl.append(only_counties.iloc[i]['POPESTIMATE2015'])
        diff = max(popl) - min(popl)
        if amax < diff:
            amax = diff
            ans = only_counties.iloc[i].name
    return ans
answer_seven()
