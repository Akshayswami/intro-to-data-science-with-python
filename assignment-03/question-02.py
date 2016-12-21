def answer_two():
    energy, GDP, ScimEn = getData()
    m1 = pd.merge(energy, GDP, how="inner", left_on="Country", right_on="Country Name")
    m2 = pd.merge(energy, ScimEn, how="inner", left_on="Country", right_on="Country")
    m3 = pd.merge(GDP, ScimEn, how="inner", left_on="Country Name", right_on="Country")
    actual = pd.merge(m1, ScimEn, how="inner", left_on="Country", right_on="Country")
    g = len(energy.index)
    r = len(GDP.index)
    p = len(ScimEn.index)
    top = len(m1.index)
    left = len(m2.index)
    right = len(m3.index)
    all3 = len(actual.index)
    ans = g + r + p - top - left - right + all3
    return ans
answer_two()
