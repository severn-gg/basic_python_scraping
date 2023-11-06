from google_play_scraper import app

import pandas as pd

import numpy as np

import pprint

from google_play_scraper import Sort, reviews_all

result = reviews_all(
    'com.app.cumobileonline',
    sleep_milliseconds=0, # defaults to 0
    lang='id', # defaults to 'en'
    country='id', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    filter_score_with=None # defaults to None(means all score)
)

df_busu = pd.DataFrame(np.array(result),columns=['review'])

df_busu = df_busu.join(pd.DataFrame(df_busu.pop('review').tolist()))

df_busu.head()

len(df_busu.index) #count the number of data we got
pprint.pprint(df_busu.index)
# df_busu[['userName', 'score','at', 'content']].head()  #preview userName, rating, date-time, and reviews only
# #Run This Code to Sort the Data By Date 

# new_df = df_busu[['userName', 'score','at', 'content']]
# sorted_df = new_df.sort_values(by='at', ascending=False) #Sort by Newst, change to True if you want to sort by Oldest.
# sorted_df.head()
# my_df = sorted_df[['userName', 'score','at', 'content']] #get userName, rating, date-time, and reviews only
# my_df.head()
# my_df.to_csv("scrapped_data.csv", index = False)  #Save the file as CSV , to download: click the folder icon on the left. the csv file should be there.