# coding: utf-8
import pandas as pd
import sys
from collections import Counter
import numpy as np
#######
import datetime
mylist = []
today = datetime.date.today()
mylist.append(today)
date = str(mylist[0]) # print the date object, not the container ;-)

##########
dist_df_name = sys.argv[1] #M1_topic_distr_df_<DATE>.csv 
lda_model_name = sys.argv[2]
topics = int(lda_model_name.split('_')[4])

#############

dist_df = pd.read_csv(dist_df_name)
counted_years = Counter(dist_df['year'])

all_means = []
for i in range(1,topics):
    print i
    all_yearly_means_topic = []
    for year, count in counted_years.items():
        year_df = dist_df.loc[dist_df['year'] == year]
        #print year
        year_mean =  np.mean(list(year_df[str(i)]))
        all_yearly_means_topic.append(year_mean)
    all_means.append(all_yearly_means_topic)

topic_disrt_df = pd.DataFrame(all_means, columns= counted_years)
topic_disrt_df_pivot  = topic_disrt_df.T
topic_disrt_df_pivot.index.name = 'Year'

topic_disrt_df_pivot.columns = [i for i in range(1,topics)]


topic_disrt_df_pivot.to_csv('M1_1_yearly_average_topic_distrbution_'+date+'.csv',  sep=',', encoding='utf-8')
print list(topic_disrt_df_pivot.index)


import matplotlib.pyplot as plt


#print topic_disrt_df_pivot.head(5)
plot = topic_disrt_df_pivot.plot( figsize=(10, 8), title= 'Average topic probability of documents', )
plot.ticklabel_format(useOffset=False)
fig = plot.get_figure()
fig.savefig("M1_sampleoutput.png")




##### python Mapping/Mapping_1_1_yearly_doc_top.dist.py topic_distr_df_2017-06-28.csv LDA_modeldata/model_2017-06-28__10_2_10_100_v-1.LDA



