import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from dax_dataframes import *
from dax_supervised import *


# Printing results of hyperparametertuning
print('results of hyperparametertuning: ',knn_cv.best_params_)
print('knn score: ',knn_cv.best_score_)
print('The accuracy is: ',knn.score(X_test, y_test))


# Create new df
merged_data = cleaned_df

def month_no_to_name(monthregex,monthname):
    """
    This function transforms the format of the date.
    Instead of a number, the month will be replaced with the 3 character abbreviation
    so it will be easier to select rows from a specific month later on
  """
    merged_data.index = merged_data.index.str.replace(monthregex,monthname, regex=True).astype('str')

month_no_to_name('\.01\.','.Jan.')
month_no_to_name('\.02\.','.Feb.')
month_no_to_name('\.03\.','.Mar.')
month_no_to_name('\.04\.','.Apr.')
month_no_to_name('\.05\.','.May.')
month_no_to_name('\.06\.','.Jun.')
month_no_to_name('\.07\.','.Jul.')
month_no_to_name('\.08\.','.Aug.')
month_no_to_name('\.09\.','.Sep.')
month_no_to_name('\.10\.','.Oct.')
month_no_to_name('\.11\.','.Nov.')
month_no_to_name('\.12\.','.Dec.')


dates = merged_data.index

jan_up = merged_data.loc[(merged_data['Up Or Down'] == 1) & dates.str.contains("Jan")]
jan_down = merged_data.loc[(merged_data['Up Or Down'] == 0) & dates.str.contains("Jan")]

feb_up = merged_data.loc[(merged_data['Up Or Down'] == 1) & dates.str.contains("Feb")]
feb_down = merged_data.loc[(merged_data['Up Or Down'] == 0) & dates.str.contains("Feb")]

mar_up = merged_data.loc[(merged_data['Up Or Down'] == 1) & dates.str.contains("Mar")]
mar_down = merged_data.loc[(merged_data['Up Or Down'] == 0) & dates.str.contains("Mar")]

apr_up = merged_data.loc[(merged_data['Up Or Down'] == 1) & dates.str.contains("Apr")]
apr_down = merged_data.loc[(merged_data['Up Or Down'] == 0) & dates.str.contains("Apr")]

may_up = merged_data.loc[(merged_data['Up Or Down'] == 1) & dates.str.contains("May")]
may_down = merged_data.loc[(merged_data['Up Or Down'] == 0) & dates.str.contains("May")]

jun_up = merged_data.loc[(merged_data['Up Or Down'] == 1) & dates.str.contains("Jun")]
jun_down = merged_data.loc[(merged_data['Up Or Down'] == 0) & dates.str.contains("Jun")]

jul_up = merged_data.loc[(merged_data['Up Or Down'] == 1) & dates.str.contains("Jul")]
jul_down = merged_data.loc[(merged_data['Up Or Down'] == 0) & dates.str.contains("Jul")]

aug_up = merged_data.loc[(merged_data['Up Or Down'] == 1) & dates.str.contains("Aug")]
aug_down = merged_data.loc[(merged_data['Up Or Down'] == 0) & dates.str.contains("Aug")]

sep_up = merged_data.loc[(merged_data['Up Or Down'] == 1) & dates.str.contains("Sep")]
sep_down = merged_data.loc[(merged_data['Up Or Down'] == 0) & dates.str.contains("Sep")]

oct_up = merged_data.loc[(merged_data['Up Or Down'] == 1) & dates.str.contains("Oct")]
oct_down = merged_data.loc[(merged_data['Up Or Down'] == 0) & dates.str.contains("Oct")]

nov_up = merged_data.loc[(merged_data['Up Or Down'] == 1) & dates.str.contains("Nov")]
nov_down = merged_data.loc[(merged_data['Up Or Down'] == 0) & dates.str.contains("Nov")]

dec_up = merged_data.loc[(merged_data['Up Or Down'] == 1) & dates.str.contains("Dec")]
dec_down = merged_data.loc[(merged_data['Up Or Down'] == 0) & dates.str.contains("Dec")]


upordown = {
    "Jan": [["1", len(jan_up)], ["0", len(jan_down)]],
    "Feb": [["1", len(feb_up)], ["0", len(feb_down)]],
    "Mar": [["1", len(mar_up)], ["0", len(mar_down)]],
    "Apr": [["1", len(apr_up)], ["0", len(apr_down)]],
    "May": [["1", len(may_up)], ["0", len(may_down)]],
    "Jun": [["1", len(jun_up)], ["0", len(jun_down)]],
    "Jul": [["1", len(jul_up)], ["0", len(jul_down)]],
    "Aug": [["1", len(aug_up)], ["0", len(aug_down)]],
    "Sep": [["1", len(sep_up)], ["0", len(sep_down)]],
    "Oct": [["1", len(oct_up)], ["0", len(oct_down)]],
    "Nov": [["1", len(nov_up)], ["0", len(nov_down)]],
    "Dec": [["1", len(dec_up)], ["0", len(dec_down)]],
}

thisdict = {
    "Up": [len(jan_up), len(feb_up), len(mar_up), len(apr_up), len(may_up), len(jun_up), len(jul_up), len(aug_up),
           len(sep_up), len(oct_up), len(nov_up), len(dec_up)],
    "Down": [len(jan_down), len(feb_down), len(mar_down), len(apr_down), len(may_down), len(jun_down), len(jul_down),
             len(aug_down), len(sep_down), len(oct_down), len(nov_down), len(dec_down)],
}

labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

data = {'Up': thisdict['Up'],
        'Down': thisdict['Down']
        }
df = pd.DataFrame.from_dict(thisdict)
df.index = labels

df.plot.barh(color=['green', 'red'])

plt.title('Up or Down by Month')
plt.ylabel('Months')
plt.xlabel('Days')
plt.show()

print('Insight 1: August is the month with the most daily losses, April is the month with the most daily gains')