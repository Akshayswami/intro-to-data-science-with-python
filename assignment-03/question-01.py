import pandas as pd
import numpy as np

def petaToGiga(row):
    row['Energy Supply'] *= 1000000
    return row

def getData():
#Reading and parsing energy ('Energy Indicators.xls')
    energy = pd.read_excel('Energy Indicators.xls', header=None, skip_footer=2)
    #print (energy)
    energy = (energy.drop([0, 1], axis=1) #Remove first two columns
                     .dropna() #drop NaN's
                     .drop(9)
                     .rename(columns={2: 'Country', #Renaming columns
                                      3: 'Energy Supply',
                                      4: 'Energy Supply per Capita',
                                      5: '% Renewable'})
                     .replace(regex=True, to_replace=[r'\d', r' \(([^)]+)\)'], value=r'') #Pruning in country names
                     .replace(to_replace=["...", "Republic of Korea", "United States of America", #Replace ... with NaN and country names
                                         "United Kingdom of Great Britain and Northern Ireland",
                                         "China, Hong Kong Special Administrative Region"],
                              value=[np.NaN, "South Korea", "United States", "United Kingdom", "Hong Kong"])
                     .apply(petaToGiga, axis=1,)) #convert petajoules to giga joules
    #print (energy)
#Reading GDP ('world_bank.csv')
    GDP = pd.read_csv('world_bank.csv', header=None, skiprows=4)
    GDP = (GDP.rename(columns=GDP.iloc[0])
              .drop(0)
              .replace(to_replace=["Korea, Rep.", "Iran, Islamic Rep.", "Hong Kong SAR, China"],
                       value=["South Korea", "Iran", "Hong Kong"])
              .rename(columns={2006: '2006', 2007: '2007', 2008: '2008', 2009: '2009', 2010: '2010',
                                    2011: '2011', 2012: '2012', 2013: '2013', 2014: '2014', 2015: '2015'}))
#Reading ScimEn('scimagojr-3.xlsx')
    ScimEn = pd.read_excel('scimagojr-3.xlsx')
    return energy, GDP, ScimEn

def answer_one():
    energy, GDP, ScimEn = getData()
    energy = energy.dropna()
    GDP_columns = ['Country Name', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    GDP = GDP[GDP_columns] #Prune GDP
    ScimEn_columns = ['Rank', 'Country', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index']
    ScimEn = ScimEn[ScimEn_columns]
    ScimEn = ScimEn[:15] #Prune ScimEn
#Merging and cleaning dataframes
    new = pd.merge(energy, GDP, how="inner", left_on="Country", right_on="Country Name")
    new = new.drop(['Country Name'], axis=1)
    new = pd.merge(new, ScimEn, how="inner", left_on='Country', right_on='Country')
    new = new.set_index('Country')
    columns = ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    new = new[columns]
    return new
answer_one()
