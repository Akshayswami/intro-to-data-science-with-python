def answer_two():
    bmax = 0
    for i in range(len(df)):
        cmax = abs(df.iloc[i]['Gold'] - df.iloc[i]['Gold.1'])
        bmax = max(bmax, cmax)
    ans = df[(abs(df['Gold'] - df['Gold.1']) == bmax)]
    return ans.iloc[0].name
answer_two()
