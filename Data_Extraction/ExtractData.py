#core python modules
import sys
import os
from nltk.stem import WordNetLemmatizer
import json
wordnet_lemmatizer = WordNetLemmatizer()


import errno
#my python code
foldername = sys.argv[1]  ## inputcorpusfolder
pos_tagging_needed = sys.argv[2] ## yes or no
#file paths original files
all_filepaths =  [os.path.join(path, name) for path, subdirs, files in os.walk(foldername) for name in files if name.endswith('xml')]
#file paths new json files

new_filepaths = [filepath.replace(foldername, 'corpus/').rstrip('.nxml')+'.json' for filepath in all_filepaths]



import extract_text_1 as et1
import POS_Tagging as pos_t
import filtering_scripts as fs



def filter_pos_tags(all_tagged_tokens, alloweditems = ['N'], numchars = 1):
    '''
    POS filtering function
    all_tagged_tokens : tagged token (Token, POS)
    alloweditems = letter with whic the POS tag starts 
    numchars = number of chraracter in the token that are considered
    
    
    '''
    return [taggeditem[0] for taggeditem in all_tagged_tokens if taggeditem[1][int(numchars)-1] in alloweditems]





for i in range( len(all_filepaths)):
    lemmatized_text = []
    text = et1.get_article_text(all_filepaths[i]) ## get article text 
    #print text
    tokenize_sentences= et1.tokenize_sent_word(text) ## tokenize sentences
    # chack if tagging is needed
    if pos_tagging_needed in ['True', 'yes', 'y', 'Y', 'Yes']:
        text_tok = pos_t.tag_tokennized_text(tokenize_sentences)
        for s in text_tok:
            for word, POStag in s:
                lemmatized = wordnet_lemmatizer.lemmatize(word), POStag
                lemmatized_text.append(lemmatized)
    else:
        for s in tokenize_sentences:
            for word in s:
                lemmatized = wordnet_lemmatizer.lemmatize(word)
                lemmatized_text.append(lemmatized)

    ### filtering
    if pos_tagging_needed in ['True', 'yes', 'y', 'Y', 'Yes']:
        filtered_pos_tokens =  filter_pos_tags(lemmatized_text)
        cleaned_text = fs.filter_spam_items(filtered_pos_tokens)

    else:
        cleaned_text = fs.filter_spam_items(lemmatized_text)

    ## corpus creation

    if not os.path.exists(os.path.dirname(new_filepaths[i])):
        try:
            os.makedirs(os.path.dirname(new_filepaths[i]))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    ### save files
    with open(new_filepaths[i], 'w') as outfile:
        json.dump(cleaned_text, outfile)
        print all_filepaths[i]
