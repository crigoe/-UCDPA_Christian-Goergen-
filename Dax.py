#importing external libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from sklearn.neighbors import KNeighborsClassifier

#importing files
from webscraping import *

#Loading dataset
data = pd.read_csv('data/DAX.csv')
df = pd.DataFrame(data)


#Print the shape of Dataframe  and Check for Null Values


# Checking for missing values
# missing_values_count = df.isnull().sum()
# print (missing_values_count)
# No missing values detected.
# print (df.shape)

Datum = str(df['Datum'])



# Analysing Data - Regex

def month_no_to_name(monthregex,monthname):
    """
       This function transforms the format of the date.
       Instead of a number, the month will be replaced with the 3 character abbreviation
       so it will be easier to select rows from a specific month later on
       """
    df['Datum'] = df['Datum'].str.replace(monthregex,monthname, regex=True).astype('str')

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



#Translating column names

df = df.rename(columns={"Datum": "Date", "Zuletzt": "Latest Price", "Eröffn.": "Open Price", "Hoch": "High", "Tief": "Low", "Vol": "Volume", "+/- %": "Change"})

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




up = df.loc[df['Up Or Down'] == 'Up']
down = df.loc[df['Up Or Down'] == 'Down']









#Maschine Learning

#y = df['Date'].values
#y = df['Up or Down'].values

# Create a k-NN classifier with 6 neighbors
#knn = KNeighborsClassifier(n_neighbors=6)

# Fit the classifier to the data
#knn.fit(X,y)




print (dax_today_int)

