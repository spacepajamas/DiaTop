# coding: utf-8
import numpy as np
import pandas as pd
import os
import json
import sys
import gensim
import re
from collections import Counter


import datetime
mylist = []
today = datetime.date.today()
mylist.append(today)
date = str(mylist[0]) # print the date object, not the container ;-)




####
lda_model_name = sys.argv[1] # LDA_modeldata/model_....LDA
foldername = sys.argv[2] # inputcorpus folder
topic_word_dist = sys.argv[3] # M2_topic_word_dist_df_DATE.csv

giventopic = sys.argv[4] # Topic number

all_filepaths =  [os.path.join(path, name) for path, subdirs, files in os.walk(foldername) for name in files if name.endswith('xml')]
relevant_filepaths = [filepath.replace(foldername, 'corpus/').rstrip('.nxml')+'.json' for filepath in all_filepaths]




model = gensim.models.ldamulticore.LdaMulticore.load(lda_model_name, mmap='r' )
topics = int(lda_model_name.split('_')[4])

all_topics = model.print_topics(topics)




def process_topics(input_string):
    '''
    from topics fro topic model 
    - get topic numer +1
    - list of topic words
    '''
    topic_list = [(topic[0], [re.sub(pattern='0.+?"', repl= '', string= item).rstrip('"')for item in topic[1].split(' + ')] )for topic in input_string]
    mytopics =  [(item[0]+1,[wj[6:] for wj in  item[1]]) for item in topic_list]
        
          #  print 
    return mytopics


## get relevan topic words

for tnum, topicwords in process_topics(all_topics):
    if tnum == int(giventopic):
        relevant_topicwords = topicwords


## topic word distribution for all topics words in the corpus 
        
all_topic_word_dist_df = pd.read_csv(topic_word_dist)
all_topic_word_dist_df.head()


## topic word distribution for topics words in the given topic 
## make data frame 
topic_df = all_topic_word_dist_df[['year']+relevant_topicwords]

counted_years = Counter(topic_df['year'])

all_means = []
for i in topic_df.columns[1:]:
    print i
    all_yearly_means_topic = []
    for year, count in counted_years.items():
        year_df = topic_df.loc[topic_df['year'] == year]
        year_mean =  np.mean(list(year_df[str(i)]))
        all_yearly_means_topic.append(year_mean)
    all_means.append(all_yearly_means_topic)


topic_word_disrt_df = pd.DataFrame(all_means, columns= counted_years)
topic_word_disrt_df_pivot  = topic_word_disrt_df.T
topic_word_disrt_df_pivot.index.name = 'Year'



topic_word_disrt_df_pivot.columns = topic_df.columns[1:]

## save data frame as csv
topic_word_disrt_df_pivot.to_csv('M2_1_Relative_frequency_topic_words_topic-'+giventopic+'_'+date+'.csv',  sep=',', encoding='utf-8')
print list(topic_word_disrt_df_pivot.index)


## plotting

import matplotlib.pyplot as plt


#print topic_disrt_df_pivot.head(5)
plot = topic_word_disrt_df_pivot.plot( figsize=(10, 8), title= 'Relative frequency of topic words' )
plot.ticklabel_format(useOffset=False)
fig = plot.get_figure()
fig.savefig("R2_sampleoutput"+date+".png")





