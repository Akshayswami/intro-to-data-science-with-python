def avg(row):
    data = row[['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
    return np.average(data)

def answer_three():
    Top15 = answer_one()
    avgGDP = Top15.apply(avg, axis=1)
    avgGDP.sort(ascending=False)
    return avgGDP
answer_three()
