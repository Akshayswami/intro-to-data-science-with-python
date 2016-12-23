import pandas as pd
import numpy as np
from scipy import stats

# Use this dictionary to map state names to two letter acronyms
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}

def get_list_of_university_towns():
    '''Returns a DataFrame of towns and the states they are in from the
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ],
    columns=["State", "RegionName"]  )

    The following cleaning needs to be done:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '\n'. '''

    df = pd.DataFrame([], columns=['State', 'RegionName'])
    with open('university_towns.txt', 'r') as f:
        state = ""
        for line in f:
            if '[edit]' in line:
                state = line[:line.find('[')].strip()
                continue
            region = line.strip()
            if '(' in region:
                region = region[:(region.find('(') - 1)]
            df = df.append(pd.DataFrame([[state, region]], columns=['State', 'RegionName']), ignore_index=True)
    return df

def get_gdp_data():
    '''Cleans GDP data in "gdplev.xls"'''

    df = pd.read_excel('gdplev.xls')
    df = (df.drop(['Current-Dollar and "Real" Gross Domestic Product',
                   'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 5'],
                  axis=1)
             .ix[7:]
             .rename(columns={'Unnamed: 4': 'Quarter', 'Unnamed: 6': 'GDP'})
             .set_index('Quarter'))
    index = df.index.get_loc('2000q1')
    df = df.ix[index:]
    return df

def get_recession_start():
    '''Returns the year and quarter of the recession start time as a
    string value in a format such as 2005q3'''

    df = get_gdp_data()
    for i in range(1, len(df) - 1):
        if (df.iloc[i]['GDP'] < df.iloc[i - 1]['GDP']) and (df.iloc[i + 1]['GDP'] < df.iloc[i]['GDP']):
            return df.iloc[i].name
    return None

def get_recession_end():
    '''Returns the year and quarter of the recession end time as a
    string value in a format such as 2005q3'''

    df = get_gdp_data()
    recession_start = get_recession_start()
    index = df.index.get_loc(recession_start)
    for i in range(index + 2, len(df)):
        if (df.iloc[i]['GDP'] > df.iloc[i - 1]['GDP']) and (df.iloc[i - 1]['GDP'] > df.iloc[i - 2]['GDP']):
            return df.iloc[i].name
    return None

def get_recession_bottom():
    '''Returns the year and quarter of the recession bottom time as a
    string value in a format such as 2005q3'''

    df = get_gdp_data()
    start = df.index.get_loc(get_recession_start())
    end = df.index.get_loc(get_recession_end())
    table = df['GDP'][start:end + 1]
    year = df[df['GDP'] == np.min(table)].iloc[0].name
    return year

def get_quarter(year, month):
    if month <= 3:
        quarter = 1
    elif month <= 6:
        quarter = 2
    elif month <= 9:
        quarter = 3
    elif month <= 12:
        quarter = 4
    return (str(year) + 'q' + str(quarter))

def convert_housing_data_to_quarters():
    '''Converts the housing data to quarters and returns it as mean
    values in a dataframe. This dataframe should be a dataframe with
    columns for 2000q1 through 2016q3, and should have a multi-index
    in the shape of ["State","RegionName"].

    Note: Quarters are defined in the assignment description, they are
    not arbitrary three month periods.

    The resulting dataframe should have 67 columns, and 10,730 rows.
    '''
    df = pd.read_csv('City_Zhvi_AllHomes.csv')
    df = (df.drop(['RegionID', 'Metro', 'CountyName', 'SizeRank'], axis=1)
             .replace({'State': states})
             .set_index(['State', 'RegionName'])
             .replace(to_replace='NaN', value=np.NaN)
             .convert_objects(convert_numeric=True)
             .sort())
    index = list(df.columns.values).index('2000-01')
    df = df.drop(df.columns[:index], axis=1)
    l = len(df.columns)
    i = 0
    while i < l:
        col_name = df.iloc[:, i].name
        year = int(col_name.split('-')[0])
        month = int(col_name.split('-')[1])
        quarter = get_quarter(year, month)
        if i + 3 < l:
            split = df.iloc[:, i:i + 3]
        else:
            split = df.iloc[:, i:l]
        df[quarter] = split.mean(axis=1)
        i += 3
    df = df.drop(df.columns[:l], axis=1)
    return df

def run_ttest():
    '''First creates new data showing the decline or growth of housing prices
    between the recession start and the recession bottom. Then runs a ttest
    comparing the university town values to the non-university towns values,
    return whether the alternative hypothesis (that the two groups are the same)
    is true or not as well as the p-value of the confidence.

    Return the tuple (different, p, better) where different=True if the t-test is
    True at a p<0.01 (we reject the null hypothesis), or different=False if
    otherwise (we cannot reject the null hypothesis). The variable p should
    be equal to the exact p value returned from scipy.stats.ttest_ind(). The
    value for better should be either "university town" or "non-university town"
    depending on which has a lower mean price ratio (which is equivilent to a
    reduced market loss).'''

    hdf = convert_housing_data_to_quarters()
    start_index = hdf.columns.get_loc(get_recession_start())
    bottom_index = hdf.columns.get_loc(get_recession_bottom())
    hdf['Ratio'] = hdf.iloc[:, start_index - 1] / hdf.iloc[:, bottom_index]
    hdf = pd.DataFrame(hdf.loc[:, 'Ratio'])
    ul = get_list_of_university_towns()
    ul = ul.set_index(['State', 'RegionName'])
    univ_prices = pd.merge(hdf, ul, how="inner", left_index=True, right_index=True)
    non_univ = pd.merge(hdf, ul, how="outer", left_index=True, right_index=True, indicator=True)
    non_univ = non_univ[non_univ['_merge'] == 'left_only']
    non_univ = non_univ.drop('_merge', axis=1)
    univ_prices = univ_prices.dropna()
    non_univ = non_univ.dropna()
    s, p = stats.ttest_ind(univ_prices['Ratio'], non_univ['Ratio'])
    s2, p2 = stats.ttest_ind(non_univ['Ratio'], univ_prices['Ratio'])
    ans = True, p, "university town"
    return ans

run_ttest()
