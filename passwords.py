import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

# ML libraries
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Importing dataset via CSV file

data = pd.read_csv('data/passwords.csv')
df = pd.DataFrame(data)

# Check for Missing Values and Duplicates
missing_values_count = df.isnull().sum()
# print (missing_values_count)

# Not all rows seem to have a value in the column 'Global_rank'.
# I am removing this column as we have a similar one "rank".
# Also, I am removing the column 'Time_to_crack' as we have another column with the same data just in a different format

df = df.drop(columns=['Global_rank','Time_to_crack'])

# Create new column "Password Length"
df['Password Length'] = df['Password'].apply(len)

# Adding a column which shows how many special characters are in the password
df['num_special']=df['Password'].apply(lambda s: len(s)-len(re.sub(r'[^0-9A-Za-z]', '', s)))

# Adding a column which shows how many vowels are in the password
df['num_vowels']=df['Password'].apply(lambda s: len(s)-len(re.sub(r'[aeiouAEIOU]', '', s)))

# Adding a column which shows how many digits are in the password
df['num_digits']=df['Password'].apply(lambda s: len(s)-len(re.sub(r'\d', '', s)))

# Adding a column with the types of passwords
type_of_passwords = []
for x in df['Password']:
    if x.isdigit():
        type_of_passwords.append('Digits only')
    elif x.isalpha():
        type_of_passwords.append('Alpha only')
    else:
        type_of_passwords.append('Mixed')

df['Type of Passwords'] = type_of_passwords
print(df.head())

#Investigating data


def cc(code):
    """
    This Function extracts the most popular passwords by country code
  """
    code = df.loc[(df['country_code'] == code)]
    code = code.drop(columns=['country', 'country_code', 'Rank', 'Time_to_crack_in_seconds', 'Password Length'])
    return code

# Creating DataFrames containing the columns "Password" and "User_count"
de = cc('de')
fr = cc('fr')
it = cc('it')


# Plotting the top10 passwords for DE, FR and IT
'''
fig, axes = plt.subplots(1, 3)

plt.suptitle("Top 10 Passwords in Germany, France and Italy")
sns.barplot(x= "User_count", y="Password", data=de.head(10), ax=axes[0])
sns.barplot(x= "User_count", y="Password", data=fr.head(10), ax=axes[1])
sns.barplot(x= "User_count", y="Password", data=it.head(10), ax=axes[2])
plt.show()

'''



# Merging DataFrames
"""
new_df = pd.merge(df1, df2, on='Columnname', how='inner')
new_df.head()
"""


# Features to create classification for password difficulty
features = df[['Time_to_crack_in_seconds','Password Length']]

X = StandardScaler().fit_transform(features)

#initialise k_means for each k
squared_distances = []
K = range(1,15)
for k in K:
    k_means = KMeans(n_clusters=k)
    model = k_means.fit(X)
    squared_distances.append(k_means.inertia_)


#Plotting sum_of_squared

plt.plot(K, squared_distances,marker='v')
plt.xlabel('k')
plt.ylabel('Squared distances')
plt.title('Check for an elbow to identify the best number of clusters')
plt.show()


# 3 gives us the best result
kmeans_3 = KMeans(n_clusters=3)
model = kmeans_3.fit(X)
predict = kmeans_3.predict(X)


# Create additional column with cluster number
df['Difficulty'] = pd.DataFrame(predict, index=df.index)

# Create lists with cat1, cat2 and cat3 pw

pwcat1 = df.loc[(df['Difficulty'] == 0)]
pwcat1 = pwcat1.drop(columns=['country', 'country_code', 'Rank'])

pwcat2 = df.loc[(df['Difficulty'] == 1)]
pwcat2 = pwcat2.drop(columns=['country', 'country_code', 'Rank'])

pwcat3 = df.loc[(df['Difficulty'] == 2)]
pwcat3 = pwcat3.drop(columns=['country', 'country_code', 'Rank'])

# Create dictionary
passwords = {'Cat1':list(pwcat1['Password']),'Cat2':list(pwcat2['Password']),'Cat3':list(pwcat3['Password'])}



