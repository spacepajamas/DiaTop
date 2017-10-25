# coding: utf-8
import pickle
import gensim
import sys
import pandas as pd

import datetime
mylist = []
today = datetime.date.today()
mylist.append(today)
date = str(mylist[0]) # print the date object, not the container ;-)


lda_corpus = sys.argv[1]
lda_model_name = sys.argv[2]
metadatafilename = sys.argv[3]

corpus = gensim.corpora.MmCorpus(lda_corpus)
model = gensim.models.ldamulticore.LdaMulticore.load(lda_model_name, mmap='r' )
print 'Get document topic document topic distribution from LDA model'
doc_topic_dist = {}
for i in range(len(corpus)):
	print len(corpus) - i, 'left'
	doc_topic_dist.update({i:model.get_document_topics(corpus[i])})

outpickelfilename = 'document_topic_distribution'+date+'.pkl'
pickle.dump(doc_topic_dist, open(outpickelfilename, 'wb'))
print 'done'
print lda_model_name.split('_')
print lda_model_name
topics = int(lda_model_name.split('_')[4])
metadata = pd.read_csv(metadatafilename)



outer_matrix = [0]*len(doc_topic_dist)
#print outer_matrix

for i in range(len(doc_topic_dist)):

    inner_list = [0]*topics
    #print i
    for v in doc_topic_dist[i]:
        inner_list[v[0]] =v[1]
        #print inner_list
    outer_matrix[i] = inner_list
#    print outer_matrix[i]
#print outer_matrix



topic_info = pd.DataFrame(outer_matrix, columns=[i for i in range(1,topics+1)])

topic_distr_df_metadata = metadata.join(topic_info, how='outer')

outputfilename = 'M1_topic_distr_df_'+date+'.csv'

topic_distr_df_metadata.to_csv(outputfilename, sep=',', encoding='utf-8', index = False)
print topic_distr_df_metadata