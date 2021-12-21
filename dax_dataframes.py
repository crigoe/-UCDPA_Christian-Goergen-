import pandas as pd

#Loading dataset
data = pd.read_csv('data/DAX.csv')
df = pd.DataFrame(data)

#Translating column names from DE to EN
df = df.rename(columns={"Datum": "Date", "Zuletzt": "Close", "Eröffn.": "Open", "Hoch": "High", "Tief": "Low", "Vol": "Vol", "+/- %": "Change"})

#Set Column index
df = df.set_index("Date")

#Create new column containing information wether the price went up or down

df['Change'] = df['Change'].str.replace(',','.')
dailychange = (df['Change'])
dailychange = [x.strip('%') for x in dailychange]

se = pd.Series(dailychange)
df['dailychange'] = se.values
df['dailychange'] = df['dailychange'].astype(float)

upordown = df['dailychange'] > 0

df['Up Or Down'] = upordown
df['Up Or Down'] = df['Up Or Down'].astype(str)
df['Up Or Down'] = df['Up Or Down'].str.replace('True','1')
df['Up Or Down'] = df['Up Or Down'].str.replace('False','0')

pd.concat([df, df['Up Or Down']], axis=1)

# Dropping necessary and helper columns
cleaned_df = df.drop(columns=['Vol.','Change','dailychange'])

#Removing ",0" and ",5" from each column
cleaned_df['Close'] = cleaned_df['Close'].str.replace(',0','')
cleaned_df['Close'] = cleaned_df['Close'].str.replace(',5','')

cleaned_df['Open'] = cleaned_df['Open'].str.replace(',0','')
cleaned_df['Open'] = cleaned_df['Open'].str.replace(',5','')

cleaned_df['High'] = cleaned_df['High'].str.replace(',0','')
cleaned_df['High'] = cleaned_df['High'].str.replace(',5','')

cleaned_df['Low'] = cleaned_df['Low'].str.replace(',0','')
cleaned_df['Low'] = cleaned_df['Low'].str.replace(',5','')

#Converting entire DataFrame into numeric values
cleaned_df = cleaned_df.apply(pd.to_numeric, errors='coerce')

x=cleaned_df[['Close', 'Open', 'High','Low']]
y=cleaned_df['Up Or Down']

# Check for Missing Values and Duplicates
missing_values_count2 = cleaned_df.isnull().sum()

#Fill missing values with previos values
cleaned_df = cleaned_df.fillna(method='ffill')
