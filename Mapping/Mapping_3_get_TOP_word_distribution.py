# coding: utf-8
import numpy as np
import pandas as pd
import os
import json
import sys
import re
from collections import Counter


####
import datetime
mylist = []
today = datetime.date.today()
mylist.append(today)
date = str(mylist[0]) # print the date object, not the container ;-)

####
topic_dist_dfname = sys.argv[1] ## M1_topic_distr_df_<DATE>.csv
lda_model_name = sys.argv[2]
num_topwords = sys.argv[3]
######
topics = int(lda_model_name.split('_')[4])
####



if not os.path.exists('M3_data'):
    os.makedirs('M3_data')

topic_dist_df = pd.read_csv(topic_dist_dfname)

print topic_dist_df


for i in range(1,topics):
    giant_array = []
    print i, '**********************'
    top1 = topic_dist_df.loc[topic_dist_df[str(i)] > 0]
    topn = pd.DataFrame(top1)
    topinc_n_filepaths =list( pd.DataFrame(topn)['new_filepaths'])
    print topinc_n_filepaths
    for relevant_file in topinc_n_filepaths:
        top_file = json.load(open(relevant_file, 'r') )
        words = [k for k,v in Counter(top_file).items() ]
        giant_array.extend(words)
    popularwords =  [popword[0] for popword in list(Counter(giant_array).most_common(int(num_topwords)))]
    outfilename = 'M3_data/M3_topic-'+str(i)+'_top_words.json'
    print outfilename
    with open(outfilename, 'w') as outfile:
        json.dump(popularwords, outfile)


    giant_array = []
    for k in range(len(topinc_n_filepaths)):
        #print i
        w_array = [0]*len(popularwords)
        for w in popularwords:
            with open(topinc_n_filepaths[k]) as json_data:
                filedata = json.load(json_data)
                #print filedata
                #print type(filedata)

                if w in filedata:
                    w_array[popularwords.index(w)] = 1
        #print w_array
        giant_array.append(np.array(w_array))

    a = np.matrix(giant_array)

    topic_word_dist = pd.DataFrame(a)
    topic_word_dist.columns = popularwords
    # print topic_word_dist
    # print pd.DataFrame(top1)
    topic_word_dist['new_filepaths'] = pd.Series(topinc_n_filepaths)
    #print topic_word_dist
    #print topn
    mid_df = pd.merge(topn,topic_word_dist,  on='new_filepaths', how='outer')
    out_df = mid_df[['year']+list(mid_df.columns[4+topics:])]

    outdfname = 'M3_data/M3_topic-'+str(i)+'_top_words.csv'
    out_df.to_csv(outdfname, sep=',', encoding='utf-8', index = False)
