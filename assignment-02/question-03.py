def answer_three():
    df2 = df[(df['Gold'] > 0) & (df['Gold.1'] > 0)]
    amax = 0
    ans = ""
    for i in range(len(df2)):
        cmax = abs(df2.iloc[i]['Gold'] - df2.iloc[i]['Gold.1'])
        cmax /= float(df2.iloc[i]['Gold.2'])
        if amax < cmax:
            amax = cmax
            ans = df2.iloc[i].name
    return ans
answer_three()
