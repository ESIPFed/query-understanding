#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 20:44:30 2017

@author: yjiang
"""

import gensim, logging, nltk, re, os, sys
from nltk.stem.lancaster import LancasterStemmer
from gensim.models import Phrases

#==============================================================================
# class Logger(object):
#     def __init__(self, filename="Default.log"):
#         self.terminal = sys.stdout
#         self.log = open(filename, "a")
# 
#     def write(self, message):
#         self.terminal.write(message)
#         self.log.write(message)
#     
#     def flush(self):
#         #this flush method is needed for python 3 compatibility.
#         #this handles the flush command by doing nothing.
#         #you might want to specify some extra behavior here.
#         pass 
# 
# sys.stdout = Logger("log.txt")
#==============================================================================

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#==============================================================================
reload(sys)
sys.setdefaultencoding('utf-8')
#==============================================================================

stopwords = nltk.corpus.stopwords.words('english')
stemmer = LancasterStemmer()

def tokenize_stem_stop(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word for word in nltk.word_tokenize(text) if word not in stopwords]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z0-9]', token):
            filtered_tokens.append(token)
    #stems = [stemmer.stem(t) for t in tokens]
    return filtered_tokens
            
#==============================================================================
# documents = ["the mayor of new york was there", "machine learning can be useful sometimes","new york mayor was present"]
# 
# sentence_stream = [doc.split(" ") for doc in documents]
# bigram = Phrases(sentence_stream, min_count=1, threshold=2)
# sent = ['new', 'york', 'was', 'there']
#==============================================================================

class MySentences(object):
     def __init__(self, dirname):
         self.dirname = dirname
  
     def __iter__(self):
         for fname in os.listdir(self.dirname):
             if not fname.startswith('.'):
                for line in open(os.path.join(self.dirname, fname)):
                    out = tokenize_stem_stop(line.lower())
                    yield out
                 
sentences = MySentences('data/')
#==============================================================================
# with open('/Users/yjiang/Documents/pythonWorkspace/data/test.txt') as f:
#     content = f.readlines()
# # you may also want to remove whitespace characters like `\n` at the end of each line
# sentences = [x.strip() for x in content] 
#==============================================================================
# print(list(sentences))
bigram = Phrases(sentences, min_count=2, threshold=2)
bi_sent = bigram[sentences]
trigram = Phrases(bigram[sentences], min_count=2, threshold=2)

#==============================================================================
# for phrase, score in trigram.export_phrases(bi_sent):
#     print(u'{0}   {1}'.format(phrase, score))
#==============================================================================

bigram.save('model/bigram')
trigram.save('model/trigram')
