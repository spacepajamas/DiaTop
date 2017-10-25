import gensim
from gensim import corpora
import logging
import os
import gensim
import json
import logging
import sys
import pickle

import datetime
mylist = []
today = datetime.date.today()
mylist.append(today)
date = str(mylist[0]) # print the date object, not the container ;-)
#########
foldername = sys.argv[1] #folder with the pre-processed corpus
indictionaryname = sys.argv[2]
##########

if not os.path.exists('LDA_modeldata'):
    os.makedirs('LDA_modeldata')



outcorpusname = 'LDA_modeldata/corp_'+date+'.corpus'

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

all_filenames =  [os.path.join(path, name) for path, subdirs, files in os.walk(foldername) for name in files if name.endswith('json')]



dictionary = gensim.corpora.Dictionary.load(indictionaryname)

class MyCorpus(object):
    def __iter__(self):
        for name in all_filenames:
            texts = json.load(open(name))#.values()[0]
            yield dictionary.doc2bow(texts)

corpus = MyCorpus()
corpora.MmCorpus.serialize(outcorpusname, corpus)
