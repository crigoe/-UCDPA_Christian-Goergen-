import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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


'''
# Plotting the top20 passwords for DE
ax = sns.barplot(x="User_count", y="Password", data=de.head(20))
plt.show()
'''

fig, axes = plt.subplots(1, 3)

plt.suptitle("Top 10 Passwords in Germany, France and Italy")
sns.barplot(x= "User_count", y="Password", data=de.head(10), ax=axes[0])
sns.barplot(x= "User_count", y="Password", data=fr.head(10), ax=axes[1])
sns.barplot(x= "User_count", y="Password", data=it.head(10), ax=axes[2])
plt.show()



# Add some bar charts showing top pw per country


#de = []
#for x in df['country_code'] == 'de':
#   de.append(x)


# Merging DataFrames

# Iterations

# Regex


# Classification


# Ml


# Visualisations