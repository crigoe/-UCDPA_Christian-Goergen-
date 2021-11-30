import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel('data/Fallzahlen_Kum_Tab.xlsx',index_col=0)
df = pd.DataFrame(data)
print (df.head())