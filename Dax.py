import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

#Loading dataset
data = pd.read_csv('../UCD_Final-Project/data/DAX.csv')
df = pd.DataFrame(data)

# Checking for missing values
missing_values_count = df.isnull().sum()
# No missing values detected.


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

#Analysis

x = cleaned_df['High']
y = cleaned_df['High']






