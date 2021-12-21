from pw_dataframes import *
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# Features to create classification for password difficulty
features = df[['Time_to_crack_in_seconds','Password Length']]

X = StandardScaler().fit_transform(features)

# Initialise k_means
squared_distances = []
K = range(1,15)
for k in K:
    k_means = KMeans(n_clusters=k)
    model = k_means.fit(X)
    squared_distances.append(k_means.inertia_)


# Plotting sum_of_squared
'''
plt.plot(K, squared_distances,marker='v')
plt.xlabel('k')
plt.ylabel('Squared distances')
plt.title('Check for an elbow to identify the best number of clusters')
plt.show()
'''

# 3 gives us the best result according to the plot (elbow method)
kmeans_3 = KMeans(n_clusters=3)
model = kmeans_3.fit(X)
predict = kmeans_3.predict(X)

# Create additional column with cluster number
df['Difficulty'] = pd.DataFrame(predict, index=df.index)

# Create dfs with cat1, cat2 and cat3 pw
pwcat1 = df.loc[(df['Difficulty'] == 0)]
pwcat1 = pwcat1.drop(columns=['country', 'country_code', 'Rank'])

pwcat2 = df.loc[(df['Difficulty'] == 1)]
pwcat2 = pwcat2.drop(columns=['country', 'country_code', 'Rank'])

pwcat3 = df.loc[(df['Difficulty'] == 2)]
pwcat3 = pwcat3.drop(columns=['country', 'country_code', 'Rank'])

# Create dictionary
passwords = {'Cat1':list(pwcat1['Password']),'Cat2':list(pwcat2['Password']),'Cat3':list(pwcat3['Password'])}

# Create lists
passwords1 = list(passwords.values())[0]
passwords2 = list(passwords.values())[1]
passwords3 = list(passwords.values())[2]


#Print cluster 1

print (passwords1)
wordcloud = WordCloud().generate(" ".join(passwords1))
# Display the generated image:
plt.figure(figsize=(10,7))
plt.title('Password Cluster 1')
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

#Print cluster 2

print (passwords2)
wordcloud = WordCloud().generate(" ".join(passwords2))
# Display the generated image:
plt.figure(figsize=(10,7))
plt.title('Password Cluster 2')
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

#Print cluster 3

print (passwords3)
wordcloud = WordCloud().generate(" ".join(passwords3))
# Display the generated image:
plt.figure(figsize=(10,7))
plt.title('Password Cluster 3')
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()