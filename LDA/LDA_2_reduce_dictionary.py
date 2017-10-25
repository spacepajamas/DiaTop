import gensim

import os
import gensim
import json
import logging
import sys
from six import iteritems

import datetime
mylist = []
today = datetime.date.today()
mylist.append(today)
date = str(mylist[0]) # print the date object, not the container ;-)





old_dictionary = sys.argv[1] # name of old dioctionary file
cutoff_n_most_frequent = int(sys.argv[2])
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

if not os.path.exists('LDA_modeldata'):
    os.makedirs('LDA_modeldata')


new_dictionary = 'LDA_modeldata/mod_dict_'+date+'.dictionary'





blacklist = ["exponential","form","10pt","article","amsmath","wasysym","amsfonts","amssymb","amsbsy","mathrsfs","pmc","euler", "fig", "upgreek","empty","document","exp","patch", "filled", "circle", "black", "line"]



def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False



def RepresentsFloat(s):

    try:
        float(s)
        return True

    except ValueError:
        return False


print 'opening dictionary...'
dictionary = gensim.corpora.Dictionary.load(old_dictionary)
print 'removing blacklist'
remove_blacklist = [ dictionary.token2id[word] for word in dictionary.token2id  if word.lower() in blacklist]
print len(remove_blacklist)
dictionary.filter_tokens(remove_blacklist)
dictionary.compactify()
print(dictionary)

print 'removing int'
remove_int = [ dictionary.token2id[word] for word in dictionary.token2id  if RepresentsInt(word) == True]
print len(remove_int)
dictionary.filter_tokens(remove_int)
dictionary.compactify()
print(dictionary)
print 'removing float'
remove_float = [ dictionary.token2id[word] for word in dictionary.token2id  if RepresentsFloat(word) == True]
print len(remove_float)

dictionary.filter_tokens(remove_float)
dictionary.compactify()
print(dictionary)

ten_times = [tokenid for tokenid, docfreq in iteritems(dictionary.dfs) if docfreq <= 10]
dictionary.filter_tokens(ten_times)

dictionary.compactify()
print(dictionary)

short_tokens = [dictionary.token2id[word] for word in dictionary.token2id if len(word) <= 3]
dictionary.filter_tokens(short_tokens)

dictionary.compactify()
print(dictionary)

latex_items = [ dictionary.token2id[word] for word in dictionary.token2id if word.startswith('\\') == True]
dictionary.filter_tokens(latex_items)

dictionary.compactify()
print(dictionary)


dictionary.filter_n_most_frequent(remove_n= cutoff_n_most_frequent)
dictionary.compactify()
print(dictionary)

gensim.corpora.Dictionary.save(dictionary, new_dictionary)
