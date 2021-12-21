#importing external libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

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

# Create arrays for the features and the response variable
y = cleaned_df['Up Or Down'].values
X = cleaned_df.drop('Up Or Down', axis=1).values

# Split into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=42, stratify=y)

'''

#Plot to determine n_neighbors

# Setup arrays to store train and test accuracies
neighbors = np.arange(1, 9)
train_accuracy = np.empty(len(neighbors))
test_accuracy = np.empty(len(neighbors))

# Loop over different values of k
for i, k in enumerate(neighbors):
    # Setup a k-NN Classifier with k neighbors: knn
    knn = KNeighborsClassifier(n_neighbors=k)

    # Fit the classifier to the training data
    knn.fit(X_train, y_train)

    # Compute accuracy on the training set
    train_accuracy[i] = knn.score(X_train, y_train)

    # Compute accuracy on the testing set
    test_accuracy[i] = knn.score(X_test, y_test)

# Generate plot
plt.title('k-NN: Varying Number of Neighbors')
plt.plot(neighbors, test_accuracy, label='Testing Accuracy')
plt.plot(neighbors, train_accuracy, label='Training Accuracy')
plt.legend()
plt.xlabel('Number of Neighbors')
plt.ylabel('Accuracy')
plt.show()

'''

# Hyperparametertuning

from sklearn.model_selection import GridSearchCV

param_grid = {'n_neighbors': np.arange(1, 50)}

knn = KNeighborsClassifier()
knn_cv = GridSearchCV(knn, param_grid, cv=5)
knn_cv.fit(X_train, y_train)

print(knn_cv.best_params_)
print(knn_cv.best_score_)

# Create a k-NN classifier with 3 neighbors
knn = KNeighborsClassifier(n_neighbors=3)

# Fit the classifier to the training data
knn.fit(X_train,y_train)

print('The accuracy is:',knn.score(X_test, y_test))