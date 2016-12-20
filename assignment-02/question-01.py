def answer_one():
    ans = df[df['Gold'] == df['Gold'].max()]
    return ans.iloc[0].name
answer_one()
