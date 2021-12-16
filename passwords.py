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


# Merging DataFrames

# Iterations

# Regex


# Classification


# Ml



# Visualisations
