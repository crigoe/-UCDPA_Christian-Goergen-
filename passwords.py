import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/passwords.csv')
df = pd.DataFrame(data)

# Check for Missing Values and Duplicates
missing_values_count = df.isnull().sum()
# print (missing_values_count)

# Not all rows seem to have a value in the column 'Global_rank', therefore, we remove this column.
# Also, I am removing the column 'Time_to_crack' as we have another column with the same data just in a different format

df = df.drop(columns=['Global_rank','Time_to_crack'])

# Create new column "Password Length"
df['Password Length'] = df['Password'].apply(len)

print(df.columns)

'''
x = df['User_count'].head(50)
y = df['Time_to_crack_in_seconds'].head(50)

plt.scatter(x,y)
plt.show()
'''


def cc(code):
    """
    This Function to extract most popular passwords by country code
  """
    code = df.loc[(df['country_code'] == code)]
    code = code.drop(columns=['country', 'country_code', 'Rank', 'Time_to_crack_in_seconds', 'Password Length'])
    print(code)

it = cc('it')
fr = cc('fr')
de = cc('de')
gb = cc('gb')
ru = cc('ru')

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