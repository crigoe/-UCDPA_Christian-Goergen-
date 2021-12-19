from passwords import *

# Top passwords which are the hardest to crack
best_passwords = df.nlargest(10, columns='Time_to_crack_in_seconds')
best_passwords = best_passwords.drop(columns=['country', 'country_code', 'Rank','User_count'])
print(best_passwords)

# Weakest passwords
weak_passwords = df.nsmallest(10, columns='Time_to_crack_in_seconds')
print(weak_passwords)


# How many passwords have special characters, vowels or digits?
print ([df['num_special'].nunique()], 'passwords have special characters')
print ([df['num_vowels'].nunique()], 'passwords have vowel characters')
print ([df['num_digits'].nunique()], 'passwords have digit characters')

# Correlation

correlation=df[['Rank','User_count', 'Time_to_crack_in_seconds', 'Password Length']].corr()
plt.imshow(correlation)


# Type of Passwords

