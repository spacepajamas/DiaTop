import os
import gensim
import json
import logging
import sys
from gensim import corpora
####
import datetime
mylist = []
today = datetime.date.today()
mylist.append(today)
date = str(mylist[0]) # print the date object, not the container ;-)

####

workers = int(sys.argv[1])
chunksize = int(sys.argv[2])
passes = int(sys.argv[3])
num_topics = int(sys.argv[4])
version = '_v-' + sys.argv[5]
indictionaryname = sys.argv[6]
incorpusfilenames = sys.argv[7]
###########
if not os.path.exists('LDA_modeldata'):
    os.makedirs('LDA_modeldata')


############

filename = 'LDA_modeldata/model_'+date+'__'+str(num_topics)+'_'+str(workers)+'_'+str(chunksize)+'_'+str(passes)+version+'.LDA'
print filename
###
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
print('loading dictionary')

dictionary = gensim.corpora.Dictionary.load(indictionaryname)


print('loading corpus...')

corpus = corpora.MmCorpus(incorpusfilenames)

print('making model...')
## with online training
lda_mcore = gensim.models.LdaMulticore(corpus, num_topics=num_topics, id2word=dictionary, workers = workers, chunksize=chunksize, passes = passes)
### no online training
#lda_mcore = gensim.models.LdaMulticore(corpus, num_topics=num_topics, id2word=dictionary, workers = workers, chunksize=chunksize, passes = passes, batch = True)

print('saving corpus...')

lda_mcore.save(filename)
