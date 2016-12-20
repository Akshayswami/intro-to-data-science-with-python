def answer_four():
    d = {}
    for i in range(len(df)):
        d[df.iloc[i].name] = df.iloc[i]['Gold.2']*3 + df.iloc[i]['Silver.2']*2 + df.iloc[i]['Bronze.2']
    return pd.Series(d)
answer_four()
