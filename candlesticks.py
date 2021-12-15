import matplotlib.pyplot as plt
import mplfinance as mpf
import pandas as pd
import matplotlib.dates as mpl_dates
import datetime
from Dax import *


daily = pd.DataFrame(
    {
        'Open': merged_data['Open'],
        'High': merged_data['High'],
        'Low': merged_data['Low'],
        'Close': merged_data['Close']
    }
)
daily['Open'] = daily['Open'].str.replace(',','')
daily['Open'] = daily['Open'].astype(float)

daily['High'] = daily['High'].str.replace(',','')
daily['High'] = daily['High'].astype(float)

daily['Low'] = daily['Low'].str.replace(',','')
daily['Low'] = daily['Low'].astype(float)

daily['Close'] = daily['Close'].str.replace(',','')
daily['Close'] = daily['Close'].astype(float)



daily['date_parsed'] = pd.to_datetime(merged_data['Date-number'], format="%d.%m.%Y")

daily.index = (daily['date_parsed'])

daily.index.name = 'Date'
mpf.plot(daily,type='candle')


q = 'How can I plot everything on one chart?'