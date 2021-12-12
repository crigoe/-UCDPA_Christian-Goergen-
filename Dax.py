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

# Checking for missing values
# missing_values_count = df.isnull().sum()
# print (missing_values_count)
# No missing values detected.

Datum = str(df['Datum'])


# Analysing Data - Regex

df['Datum'] = df['Datum'].str.replace('\.01\.', '.Jan.',regex=True).astype('str')
df['Datum'] = df['Datum'].str.replace('\.02\.', '.Feb.',regex=True).astype('str')
df['Datum'] = df['Datum'].str.replace('\.03\.', '.Mar.',regex=True).astype('str')
df['Datum'] = df['Datum'].str.replace('\.04\.', '.Apr.',regex=True).astype('str')
df['Datum'] = df['Datum'].str.replace('\.05\.', '.May.',regex=True).astype('str')
df['Datum'] = df['Datum'].str.replace('\.06\.', '.Jun.',regex=True).astype('str')
df['Datum'] = df['Datum'].str.replace('\.07\.', '.Jul.',regex=True).astype('str')
df['Datum'] = df['Datum'].str.replace('\.08\.', '.Aug.',regex=True).astype('str')
df['Datum'] = df['Datum'].str.replace('\.09\.', '.Sep.',regex=True).astype('str')
df['Datum'] = df['Datum'].str.replace('\.10\.', '.Oct.',regex=True).astype('str')
df['Datum'] = df['Datum'].str.replace('\.11\.', '.Nov.',regex=True).astype('str')
df['Datum'] = df['Datum'].str.replace('\.12\.', '.Dec.',regex=True).astype('str')




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

