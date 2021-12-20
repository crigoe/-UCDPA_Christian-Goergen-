#importing external libraries
import pandas as pd
import numpy as np

#Loading dataset
data = pd.read_csv('data/DAX.csv')
df = pd.DataFrame(data)

vix = pd.read_csv('data/vix.csv')
vix_df = pd.DataFrame(vix)
vix_df = vix.drop(columns=['Zuletzt','Eröffn.','Hoch','Tief','Vol.'])

vix_df = vix_df.rename(columns={"Datum": "Date", "+/- %": "VIX"})

vix_df = vix_df.set_index("Date")
vix_df['VIX'] = vix_df['VIX'].str.replace(',','.')


volindex = (vix_df['VIX'])
volindex = [x.strip('%') for x in volindex]
vix_df['VIX'] = volindex
vix_df['VIX'] = vix_df['VIX'].astype(float)


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
df['Up Or Down'] = df['Up Or Down'].str.replace('True','1')
df['Up Or Down'] = df['Up Or Down'].str.replace('False','0')


pd.concat([df, df['Up Or Down']], axis=1)

cleaned_df = df.drop(columns="dailychange")


#Merging two DataFrames
merged_data= pd.merge(cleaned_df,vix_df,on='Date')



x=merged_data[['Close', 'Open', 'High','Low','Change','VIX']]
y=merged_data['Up Or Down']



print(x)
print(y)

'''# Import KNeighborsClassifier from sklearn.neighbors
from sklearn.neighbors import KNeighborsClassifier

# Create arrays for the features and the response variable
y = merged_data['Up Or Down'].values
X = df.drop('Up Or Down', axis=1).values

merged_data.apply(pd.to_numeric)

print(merged_data.info)
# Create a k-NN classifier with 6 neighbors
knn = KNeighborsClassifier(n_neighbors=6)

# Fit the classifier to the data
knn.fit(X,y)


# Predict the labels for the training data X
y_pred = knn.predict(X)

# Predict and print the label for the new data point X_new
X_new = pd.DataFrame(np.array(["16.246,0","16.130,0","16.261,0","16.112,0","60,33K","0,71%"]),
                   columns=['Close', 'Open', 'High', 'Low', 'Vol.', 'Change', 'Up Or Down', 'VIX'])

new_prediction = knn.predict(X_new)
print("Prediction: {}".format(new_prediction))
'''