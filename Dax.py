import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

#Loading dataset
data = pd.read_csv('data/DAX.csv')
df = pd.DataFrame(data)

# Checking for missing values
missing_values_count = df.isnull().sum()
# print (missing_values_count)
# No missing values detected.

Datum = str(df['Datum'])
output = re.findall("\.11\.", Datum)
print (output.head())





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



jan = '\.01\.'
feb = '\.02\.'
mar = '\.03\.'
apr = '\.04\.'
may = '\.05\.'
jun = '\.06\.'
jul = '\.07\.'
aug = '\.08\.'
sep = '\.09\.'
oct = '\.10\.'
nov = '\.11\.'
dec = '\.12\.'









