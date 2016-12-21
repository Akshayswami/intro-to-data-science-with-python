def answer_five():
    Top15 = answer_one()
    avg = np.average(Top15['Energy Supply per Capita'])
    return float(avg)
answer_five()
