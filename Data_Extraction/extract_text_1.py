import xml.etree.cElementTree as ET
import json
import sys
import os

from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk import sent_tokenize
from string import punctuation
from nltk.stem import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()
punc = list(punctuation)
sw = stopwords.words('english')




def get_article_text( filepath):
    
    '''
    filters and gets articles text from the XML file
    '''

    list1 = []
    list2 = []
    blackList = ['disp-formula', 'sub','label','caption','sup','title','xref','tex-math', 'table', 'table-wrap', 'th', 'tr','thead', 'tbody', 'fig', 'td', 'graphic', 'xef']
    root = ET.XML(open(filepath).read())

    for e in root.findall('.//sec') :
        for item in e:
            list1.extend(list(item.itertext()))
        for i in item.iter():
            if  i.tag in blackList:
                list2.append( i.text)

    return ' '.join([item for item in list1 if item not in list2])


def tokenize_sent_word(textstring):
    '''
    textstring = string that will be tokenized
    '''
    sentences = sent_tokenize(textstring)
    #print sentences
    word_tokenized_sentences = [word_tokenize(sent) for sent in sentences]
    #print word_tokenized_sentences
    return word_tokenized_sentences


