def answer_eight():
    new = census_df.where((census_df['REGION'] == 1) | (census_df['REGION'] == 2))
    new = new.dropna()
    columns_to_keep = ['STNAME', 'CTYNAME', 'POPESTIMATE2014', 'POPESTIMATE2015']
    new = new[columns_to_keep]
    i = 0
    while i < len(new):
        county = new.iloc[i]['CTYNAME']
        if 'Washington' not in county:
            new = new.drop(new.index[i])
        else:
            i += 1
    new = new.where(new['POPESTIMATE2015'] > new['POPESTIMATE2014'])
    new = new.dropna()
    new = new[['STNAME', 'CTYNAME']]
    new.sort_index(inplace=True)
    return new
answer_eight()
