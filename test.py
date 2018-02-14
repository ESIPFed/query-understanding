#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 20:36:41 2017

@author: yjiang
"""

import gensim, logging, nltk, re, os, sys
from nltk.stem.lancaster import LancasterStemmer
from gensim.models import Phrases

bigram = Phrases.load('model/bigram')
trigram = Phrases.load('model/trigram')
sent = ['sea', 'surface', 'temperature', 'modis', 'level', '2', 'pacific', 'ocean']

print(trigram[bigram[sent]])