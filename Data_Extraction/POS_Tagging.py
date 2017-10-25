# -*- coding: utf-8 -*-
from nltk import pos_tag
from nltk import word_tokenize
from nltk import sent_tokenize


def tag_tokennized_text(list_of_tokenized_sentences):
    return [pos_tag(tok_sent) for tok_sent in list_of_tokenized_sentences]

#print [tag_tokennized_text(word) for item in sent_tokenize(text) for word in item]
