from pw_dataframes import *
import matplotlib.pyplot as plt
import seaborn as sns

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

# Password Length
plt.hist(df['Password Length'],bins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
plt.title('Distribution of Password Length')
plt.show()

# Plotting the top10 passwords for DE, FR and IT
f, (ax1, ax2, ax3) = plt.subplots(3, 1)
plt.suptitle("Top 10 Passwords in Germany, France and Italy")

sns.barplot(x= "User_count", y="Password", data=de.head(10), palette="rocket", ax=ax1)
sns.barplot(x= "User_count", y="Password", data=fr.head(10), palette="rocket", ax=ax2)
sns.barplot(x= "User_count", y="Password", data=it.head(10), palette="rocket", ax=ax3)

plt.show()