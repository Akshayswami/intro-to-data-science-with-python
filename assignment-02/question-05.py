def answer_five():
    only_counties = census_df.where(census_df['SUMLEV'] == 50)
    only_counties = only_counties.dropna()
    freq = only_counties['STNAME'].value_counts()
    return freq[freq == freq.max()].index[0]
answer_five()
