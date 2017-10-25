from nltk.corpus import stopwords
from string import punctuation

punc = list(punctuation)
sw = stopwords.words('english')




def remove_punc(input_string):
    """
    removes punctuation
    """
    if input_string not in punc:
        return input_string

def remove_end_punc( input_string):
    """
    removes end of token punctuation
    """

    
    if input_string[-1] not in punc:
        return input_string


def remove_start_punc( input_string):
    """
    removes beginning of token punctuation
    """


    if input_string[0] not in punc:
        return input_string

def remove_stopwords( input_string):
    """
    removes stop words
    """
    

    if input_string not in sw:
        return input_string

def remove_small_words(input_string, n = 2):
    """
    removes small tokens
    default value n = 2,
    n : size of token
    """


    if len(input_string) >= n:
        return input_string

def RepresentsInt(input_string):
    """
    checks if string is integer
    if true returns None
    """
    try:
        int(input_string)
        return None
    except ValueError:
        return input_string

def RepresentsFloat(input_string):
    """
    checks if string is float
    if true returns None
    """    
    try:
        float(input_string)
        return None
    except ValueError:
        return input_string








def filter_spam_items(tokenized):
    '''
    runs the the fuctions above on the list of tokens.
    returns clean list of tokens
    tokenized : list of tokens
    '''
    tokenized_lower = map(lambda x:x.lower(),tokenized)
    endpunc_removed = filter(None, map(remove_end_punc, tokenized_lower))
    startpunc_removed = filter(None, map(remove_start_punc, endpunc_removed))
    punc_removed = filter(None, map(remove_punc, startpunc_removed))
    stopwords_removed = filter(None, map(remove_stopwords, punc_removed))
    cleaned_Int = filter(None, map(RepresentsInt, stopwords_removed))
    cleaned_Float = filter(None, map(RepresentsFloat, cleaned_Int))
    cleaned_small_words = filter(None, map(remove_small_words, cleaned_Float))

    return cleaned_small_words
