import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from dax_dataframes import *

# Printing results of hyperpara
#print(knn_cv.best_params_)
#print(knn_cv.best_score_)
#print('The accuracy is:',knn.score(X_test, y_test))


#Merging two DataFrames
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

jan_up = merged_data.loc[(merged_data['Up Or Down'] == 'Up') & dates.str.contains("Jan")]
jan_down = merged_data.loc[(merged_data['Up Or Down'] == 'Down') & dates.str.contains("Jan")]

feb_up = merged_data.loc[(merged_data['Up Or Down'] == 'Up') & dates.str.contains("Feb")]
feb_down = merged_data.loc[(merged_data['Up Or Down'] == 'Down') & dates.str.contains("Feb")]

mar_up = merged_data.loc[(merged_data['Up Or Down'] == 'Up') & dates.str.contains("Mar")]
mar_down = merged_data.loc[(merged_data['Up Or Down'] == 'Down') & dates.str.contains("Mar")]

apr_up = merged_data.loc[(merged_data['Up Or Down'] == 'Up') & dates.str.contains("Apr")]
apr_down = merged_data.loc[(merged_data['Up Or Down'] == 'Down') & dates.str.contains("Apr")]

may_up = merged_data.loc[(merged_data['Up Or Down'] == 'Up') & dates.str.contains("May")]
may_down = merged_data.loc[(merged_data['Up Or Down'] == 'Down') & dates.str.contains("May")]

jun_up = merged_data.loc[(merged_data['Up Or Down'] == 'Up') & dates.str.contains("Jun")]
jun_down = merged_data.loc[(merged_data['Up Or Down'] == 'Down') & dates.str.contains("Jun")]

jul_up = merged_data.loc[(merged_data['Up Or Down'] == 'Up') & dates.str.contains("Jul")]
jul_down = merged_data.loc[(merged_data['Up Or Down'] == 'Down') & dates.str.contains("Jul")]

aug_up = merged_data.loc[(merged_data['Up Or Down'] == 'Up') & dates.str.contains("Aug")]
aug_down = merged_data.loc[(merged_data['Up Or Down'] == 'Down') & dates.str.contains("Aug")]

sep_up = merged_data.loc[(merged_data['Up Or Down'] == 'Up') & dates.str.contains("Sep")]
sep_down = merged_data.loc[(merged_data['Up Or Down'] == 'Down') & dates.str.contains("Sep")]

oct_up = merged_data.loc[(merged_data['Up Or Down'] == 'Up') & dates.str.contains("Oct")]
oct_down = merged_data.loc[(merged_data['Up Or Down'] == 'Down') & dates.str.contains("Oct")]

nov_up = merged_data.loc[(merged_data['Up Or Down'] == 'Up') & dates.str.contains("Nov")]
nov_down = merged_data.loc[(merged_data['Up Or Down'] == 'Down') & dates.str.contains("Nov")]

dec_up = merged_data.loc[(merged_data['Up Or Down'] == 'Up') & dates.str.contains("Dec")]
dec_down = merged_data.loc[(merged_data['Up Or Down'] == 'Down') & dates.str.contains("Dec")]

upordown = {
    "Jan": [["Up", len(jan_up)], ["Down", len(jan_down)]],
    "Feb": [["Up", len(feb_up)], ["Down", len(feb_down)]],
    "Mar": [["Up", len(mar_up)], ["Down", len(mar_down)]],
    "Apr": [["Up", len(apr_up)], ["Down", len(apr_down)]],
    "May": [["Up", len(may_up)], ["Down", len(may_down)]],
    "Jun": [["Up", len(jun_up)], ["Down", len(jun_down)]],
    "Jul": [["Up", len(jul_up)], ["Down", len(jul_down)]],
    "Aug": [["Up", len(aug_up)], ["Down", len(aug_down)]],
    "Sep": [["Up", len(sep_up)], ["Down", len(sep_down)]],
    "Oct": [["Up", len(oct_up)], ["Down", len(oct_down)]],
    "Nov": [["Up", len(nov_up)], ["Down", len(nov_down)]],
    "Dec": [["Up", len(dec_up)], ["Down", len(dec_down)]],
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