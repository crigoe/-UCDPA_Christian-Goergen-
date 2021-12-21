import numpy as np
import pandas as pd
import re

# Importing dataset via CSV file
data = pd.read_csv('data/passwords.csv')
df = pd.DataFrame(data)

# Check for Missing Values and Duplicates
missing_values_count = df.isnull().sum()
# print (missing_values_count)

'''
Not all rows seem to have a value in the column 'Global_rank'.
I am removing this column as we have a similar one "rank".
Also, I am removing the column 'Time_to_crack' as we have another column containing that data
'''

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

def cc(code):
    """
    This Function extracts the most popular passwords by country code
  """
    code = df.loc[(df['country_code'] == code)]
    code = code.drop(columns=['country', 'Rank', 'num_vowels','num_digits','num_special','Type of Passwords','Time_to_crack_in_seconds', 'Password Length'])
    return code

# Creating DataFrames containing the columns "Password" and "User_count"
de = cc('de')
fr = cc('fr')
it = cc('it')

# Merging DataFrames using concat()
top_defrit = pd.concat([de, fr,it])