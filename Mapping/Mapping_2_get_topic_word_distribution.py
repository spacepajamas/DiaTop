# coding: utf-8
import numpy as np
import pandas as pd
import os
import json
import xml.etree.cElementTree as ET
import sys
import gensim
import re


####
import datetime
mylist = []
today = datetime.date.today()
mylist.append(today)
date = str(mylist[0]) # print the date object, not the container ;-)

####
lda_model_name = sys.argv[1]
foldername = sys.argv[2] ## original corpus folder
metadatafilename = sys.argv[3]





#filesnames = json.load(open('all_150K_filepaths.json', 'r') )
all_filepaths =  [os.path.join(path, name) for path, subdirs, files in os.walk(foldername) for name in files if name.endswith('xml')]
relevant_filepaths = [filepath.replace(foldername, 'corpus/').rstrip('.nxml')+'.json' for filepath in all_filepaths]

#print relevant_filepaths



#metadatafilename = sys.argv[2]


model = gensim.models.ldamulticore.LdaMulticore.load(lda_model_name, mmap='r' )
topics = int(lda_model_name.split('_')[4])

all_topics = model.print_topics(topics)




def process_topics(input_string):
    '''
    process topicmodel input_string
    '''
    topic_list = [(topic[0], [re.sub(pattern='0.+?"', repl= '', string= item).rstrip('"')for item in topic[1].split(' + ')] )for topic in input_string]

    tw = list(set([ w.split('*')[1]for topic in topic_list for top in topic[1:] for w in top]))
    return tw



word_list =  sorted(process_topics(all_topics))
print word_list
giant_array = []
for i in range(len(relevant_filepaths)):
    #print i
    w_array = [0]*len(word_list)
    for w in word_list:
        with open(relevant_filepaths[i]) as json_data:
            filedata = json.load(json_data)
            #print filedata
            #print type(filedata)

            if w in filedata:
                w_array[word_list.index(w)] = 1
    #print w_array
    giant_array.append(np.array(w_array))


#print giant_array
a = np.matrix(giant_array)

topic_word_dist = pd.DataFrame(a)
#print topic_word_dist
#print '****************'
topic_word_dist.columns = word_list

#print topic_word_dist
############3
metadata = pd.read_csv(metadatafilename)

#
#
topic_word_dist_metadata = metadata.join(topic_word_dist, how='outer')

outputfilename = 'M2_topic_word_dist_df_'+date+'.csv'

topic_word_dist_metadata.to_csv(outputfilename, sep=',', encoding='utf-8', index = False)



print topic_word_dist_metadata
