import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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


#Investigating data


# How many weak passwords consist of 6 numbers only?

weakpassword = ['ekfkefkfekekfekef']


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


# Plotting the top20 passwords for DE
'''
fig, axes = plt.subplots(1, 3)

plt.suptitle("Top 10 Passwords in Germany, France and Italy")
sns.barplot(x= "User_count", y="Password", data=de.head(10), ax=axes[0])
sns.barplot(x= "User_count", y="Password", data=fr.head(10), ax=axes[1])
sns.barplot(x= "User_count", y="Password", data=it.head(10), ax=axes[2])
plt.show()
'''

# Merging DataFrames

# Iterations



# Classification


# Two features to create classification for password difficulty
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
'''
plt.plot(K, squared_distances,marker='v')
plt.xlabel('k')
plt.ylabel('Squared distances')
plt.title('Check for an elbow to identify the best number of clusters')
plt.show()
'''

# 3 gives us the best result
kmeans_3 = KMeans(n_clusters=3)
model = kmeans_3.fit(X)
predict = kmeans_3.predict(X)


# Create additional column with cluster number
df['Difficulity'] = pd.DataFrame(predict, index=df.index)


# Create lists with cat1, cat2 and cat3 pw
cat1pw = []
cat2pw = []
cat3pw = []

