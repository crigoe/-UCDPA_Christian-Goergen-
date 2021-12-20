import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing data from https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Daten/Ausbruchsdaten.html
data = pd.read_excel('Ausbruchsdaten.xlsx',index_col=3)
df = pd.DataFrame(data)

# Removing data from 2020 and picking the dataset of current week

last_week = 51

df_cleaned = df[df.Meldejahr != 2020]
df_cleaned = df[df.Meldewoche == last_week]

# Dropping "Meldejahr" and "sett_f" columns
df_cleaned = df_cleaned.drop('Meldejahr', 1)
df_cleaned = df_cleaned.drop('sett_f', 1)
df_cleaned = df_cleaned.drop(index='Not documented in an outbreak')


# Sorting
infections = df_cleaned.sort_values(by=['n'], ascending=True)

# Plot
x = infections.index
y = infections['n']

plt.rcParams.update({'figure.autolayout': True})

fig, ax = plt.subplots()
plt.style.use('_mpl-gallery')

ax.barh(x, y)
ax.set_xlabel('Number of confirmed cases')
ax.set_title('Where people caught covid in Week '+str(last_week))

plt.show()