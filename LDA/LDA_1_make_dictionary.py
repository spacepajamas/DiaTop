import gensim
import os
import gensim
import json
import logging
import sys
from six import iteritems
from gensim import corpora
import datetime
mylist = []
today = datetime.date.today()
mylist.append(today)
date = str(mylist[0]) # print the date object, not the container ;-)


foldername = sys.argv[1] ## 'corpus' folder

if not os.path.exists('LDA_modeldata'):
    os.makedirs('LDA_modeldata')


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
all_filenames =  [os.path.join(path, name) for path, subdirs, files in os.walk(foldername) for name in files if name.endswith('json')]

print 'making  dictionary'
dictionary = gensim.corpora.Dictionary([json.load(open(name)) for name in all_filenames[0:]] )
print(dictionary)

## code for adding documents at a smaller rate
# use if adding a huge amount of texts i.e. +10K document
# set n factor of len(all_filenames), is an integer which evenly divides len(all_filenames) without leaving a remainder
'''
dictionary = gensim.corpora.Dictionary([json.load(open(name)) for name in all_filenames[0:n]] )

for i in range(n,int(all_filenames),n): 
    print 'adding more data to the dictionary...'
    print i, i+n
    dictionary.add_documents([json.load(open(name)).values()[0] for name in all_filenames[i: i+n]])
    print(dictionary)
'''

print('making file')
gensim.corpora.Dictionary.save(dictionary, 'LDA_modeldata/original_dict_'+date+'.dictionary')
