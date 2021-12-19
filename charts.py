import seaborn as sns
import matplotlib.pyplot as plt
from passwords import *

# Password Length
plt.hist(df['Password Length'],bins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
plt.title('Distribution of Password Length')

# Type of Passwords
plt.title('Type of Passwords')
sns.catplot("Type of Passwords", data=df, kind="count")

# Correlation between columns
pwcorr = df.iloc[:,5:]
fig, ax = plt.subplots()
sns.heatmap(pwcorr.corr(), linewidths=.5, ax=ax)
plt.show()