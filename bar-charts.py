import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")
from passwords import *

passwords_de = pd.DataFrame(de)
print (passwords_de)

# Initialize the matplotlib figure
f, ax = plt.subplots(figsize=(6, 15))

# Load the example car crash dataset
crashes = sns.load_dataset("car_crashes").sort_values("total", ascending=False)

# Plot the crashes where alcohol was involved
sns.set_color_codes("muted")
sns.barplot(x="User_count", y="Password", data=de,
            label="Most used Passwords", color="b")

# Add a legend and informative axis label
ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(xlim=(0, 24), ylabel="",
       xlabel="Automobile collisions per billion miles")
sns.despine(left=True, bottom=True)

plt.show()