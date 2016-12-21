def answer_nine():
    Top15 = answer_one().copy()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    Top15 = Top15.corr(method='pearson')
    ans = Top15.loc['Energy Supply per Capita', 'Citable docs per Capita']
    return ans
answer_nine()
