import matplotlib.pyplot as plt

from passwords import *


plt.hist(df['Password Length'],bins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
plt.title('Distribution of Password Length')
plt.show()


