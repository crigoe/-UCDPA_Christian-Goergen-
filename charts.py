import numpy as np
import matplotlib.pyplot as plt
from Dax import *

"""
  
fig, ax = plt.subplots()


x = np.array(merged_data['VIX'].head(20))
y = np.array(merged_data['Change'].head(20))

plt.scatter(x, y)
ax.set_xlabel('Vix', fontsize=15)
ax.set_ylabel('Change', fontsize=15)
ax.set_title('Volume and percent change')

ax.grid(True)
fig.tight_layout()

plt.show()

 """



up = merged_data.loc[merged_data['Up Or Down'] == 'Up' & merged_data.index == 'Jan']
down = merged_data.loc[merged_data['Up Or Down'] == 'Down']


print (up)

jan = []
tue = []
wed = []
thu = []
fri = []