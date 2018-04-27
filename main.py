#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 20:36:41 2017

@author: yjiang
"""

import gensim, logging, nltk, re, os, sys
from nltk.stem.lancaster import LancasterStemmer
from gensim.models import Phrases
from temporalParsing import *
from geoParsing import *

def phraseDetect(query):
    bigram = Phrases.load('model/bigram')
    trigram = Phrases.load('model/trigram')
    #sent = ['sea', 'surface', 'temperature', 'modis', 'level', '2', 'pacific', 'ocean']
    return trigram[bigram[query.split()]]

def deepQuery(query):
    res= {}
    res['geo'] = geoParse(query)
    res['time'] = temporalParse(query)
    res['phrase'] = phraseDetect(query)
    return res

testQ = 'sea surface temperature modis level 2 pacific ocean in March 3rd, 2004'
print(deepQuery(testQ))

#testing result: {'phrase': [u'sea_surface_temperature', u'modis', u'level_2', u'pacific_ocean', u'in', u'March', u'3rd,', u'2004'], 
#'geo': {u'northeast': {u'lat': 48.7297227, u'lng': -122.4090338}, u'southwest': {u'lat': 48.717229, u'lng': -122.416576}}, 
#'time': [(u'in March 3rd, 2004', datetime.datetime(2004, 3, 3, 0, 0))]}
    