from pw_dataframes import *
import matplotlib.pyplot as plt
import seaborn as sns

# Top passwords which are the hardest to crack
best_passwords_df = df.nlargest(10, columns='Time_to_crack_in_seconds')
best_passwords = best_passwords_df['Password'].tolist()
print('Insight 2: The Top10 passwords which are the hardest to crack are: ',best_passwords)

# Weakest passwords
weak_passwords_df = df.nsmallest(10, columns='Time_to_crack_in_seconds')
weak_passwords = weak_passwords_df['Password'].tolist()
print('Insight 3: The 10 weakest passwords which are the easiest to crack are: ',weak_passwords)

print('Insight 4: Most passwords have 6 characters')
print('Insight 5: 123456 is the most used password in Germany, France and Italy')


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