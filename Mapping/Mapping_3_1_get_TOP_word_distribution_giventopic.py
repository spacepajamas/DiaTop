import numpy as np
import pandas as pd
import os
import json
import sys
import gensim
import re
from collections import Counter

####
import datetime
mylist = []
today = datetime.date.today()
mylist.append(today)
date = str(mylist[0]) # print the date object, not the container ;-)

######

lda_model_name = sys.argv[1] #'LDA_modeldata/model_<params>.LDA'#
giventopic = sys.argv[2] # topic number
popular_topic_word_dist = 'M3_data/M3_topic-'+giventopic+'_top_words.csv'#sys.argv[3]



all_popular_topic_word_dist_df = pd.read_csv(popular_topic_word_dist)

counted_years = Counter(all_popular_topic_word_dist_df['year'])

all_means = []
for i in all_popular_topic_word_dist_df.columns[1:]:
    print i
    all_yearly_means_topic = []
    for year, count in counted_years.items():
        year_df = all_popular_topic_word_dist_df.loc[all_popular_topic_word_dist_df['year'] == year]
        #print year
        year_mean =  np.mean(list(year_df[str(i)]))
        all_yearly_means_topic.append(year_mean)
    all_means.append(all_yearly_means_topic)


topic_word_disrt_df = pd.DataFrame(all_means, columns= counted_years)
topic_word_disrt_df_pivot  = topic_word_disrt_df.T
topic_word_disrt_df_pivot.index.name = 'Year'


topic_word_disrt_df_pivot.columns = all_popular_topic_word_dist_df.columns[1:]


topic_word_disrt_df_pivot.to_csv('M3_data/M3_1_Relative_frequency_popular_words_topic-'+giventopic+'_'+date+'.csv',  sep=',', encoding='utf-8')
print list(topic_word_disrt_df_pivot.index)



import matplotlib.pyplot as plt


#print topic_disrt_df_pivot.head(5)
plot = topic_word_disrt_df_pivot.plot( figsize=(10, 8), title= 'Relative frequency of topic words' )
plot.ticklabel_format(useOffset=False)
fig = plot.get_figure()
fig.savefig("M3_sampleoutput"+date+".png")





















