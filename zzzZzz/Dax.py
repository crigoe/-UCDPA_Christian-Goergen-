#importing external libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from sklearn.neighbors import KNeighborsClassifier

#importing files
#from webscraping import *
#print (dax_today_int)

#Loading dataset
data = pd.read_csv('DAX.csv')
df = pd.DataFrame(data)

vix = pd.read_csv('vix.csv')
vix_df = pd.DataFrame(vix)
vix_df = vix.drop(columns=['Zuletzt','Eröffn.','Hoch','Tief','Vol.'])

vix_df = vix_df.rename(columns={"Datum": "Date", "+/- %": "VIX"})

vix_df = vix_df.set_index("Date")
vix_df['VIX'] = vix_df['VIX'].str.replace(',','.')


volindex = (vix_df['VIX'])
volindex = [x.strip('%') for x in volindex]
vix_df['VIX'] = volindex
vix_df['VIX'] = vix_df['VIX'].astype(float)

# Checking for missing values
#missing_values_count_vix = vix_df.isnull().sum()
#print (missing_values_count_vix)
#print (vix_df.shape)
#No missing values detected.






# Checking for missing values
# missing_values_count = df.isnull().sum()
# print (missing_values_count)
# No missing values detected.
# print (df.shape)

Datum = str(df['Datum'])



#Translating column names

df = df.rename(columns={"Datum": "Date", "Zuletzt": "Close", "Eröffn.": "Open", "Hoch": "High", "Tief": "Low", "Vol": "Vol", "+/- %": "Change"})

df = df.set_index("Date")
df['Change'] = df['Change'].str.replace(',','.')


dailychange = (df['Change'])
dailychange = [x.strip('%') for x in dailychange]

# Add new column to dataframe
se = pd.Series(dailychange)
df['dailychange'] = se.values
df['dailychange'] = df['dailychange'].astype(float)



upordown = df['dailychange'] > 0

df['Up Or Down'] = upordown
df['Up Or Down'] = df['Up Or Down'].astype(str)
df['Up Or Down'] = df['Up Or Down'].str.replace('True','Up')
df['Up Or Down'] = df['Up Or Down'].str.replace('False','Down')

pd.concat([df, df['Up Or Down']], axis=1)

cleaned_df = df.drop(columns="dailychange")






cleaned_df['Date-number'] = cleaned_df.index


#Merging two DataFrames
merged_data= pd.merge(cleaned_df,vix_df,on='Date')




#missing_values_count = merged_data.isnull().sum()
#print (missing_values_count)
#print (merged_data.shape)
#No missing values detected.



def month_no_to_name(monthregex,monthname):
    """
    This function transforms the format of the date.
    Instead of a number, the month will be replaced with the 3 character abbreviation
    so it will be easier to select rows from a specific month later on
  """
    merged_data.index = merged_data.index.str.replace(monthregex,monthname, regex=True).astype('str')

month_no_to_name('\.01\.','.Jan.')
month_no_to_name('\.02\.','.Feb.')
month_no_to_name('\.03\.','.Mar.')
month_no_to_name('\.04\.','.Apr.')
month_no_to_name('\.05\.','.May.')
month_no_to_name('\.06\.','.Jun.')
month_no_to_name('\.07\.','.Jul.')
month_no_to_name('\.08\.','.Aug.')
month_no_to_name('\.09\.','.Sep.')
month_no_to_name('\.10\.','.Oct.')
month_no_to_name('\.11\.','.Nov.')
month_no_to_name('\.12\.','.Dec.')



#Maschine Learning

#y = df['Date'].values
#y = df['Up or Down'].values

# Create a k-NN classifier with 6 neighbors
#knn = KNeighborsClassifier(n_neighbors=6)

# Fit the classifier to the data
#knn.fit(X,y)




#Charts


