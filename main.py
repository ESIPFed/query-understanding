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
from semanticAnalysis import *

def phraseDetect(query):
    bigram = Phrases.load('model/bigram')
    trigram = Phrases.load('model/trigram')
    return trigram[bigram[query.split()]]

def deepQuery(query):
    res= {}
    
    #temporal parsing
    res['time'] = temporalParse(query)
    query = query.replace(str(res['time'][0][0]), '')
    
    #geoparsing
    geo = geoParse(query)
    res['geo'] = geo['bounds']
    query = query.replace(str(geo['string']).lower(), '')
    
    #query expansion
    res['phrase'] = phraseDetect(query.strip())
    
    #semantic expansion, just to expand the first phrase as an example
    phrase = str(res['phrase'][0])
    res['semantics'] = expandQuery(phrase.replace('_', ' '))
    return res

testQ = 'sea surface temperature modis level 2 pacific ocean in March 3rd, 2004'
print(deepQuery(testQ))

# example output
# {'phrase': [u'sea_surface_temperature', u'modis', u'level_2'], 
# 'geo': {u'northeast': {u'lat': 59.48222930000001, u'lng': -66.51908139999999}, u'southwest': {u'lat': -77.8225785, u'lng': 128.576489}}, 
# 'semantics': {u'graph': {u'ontology': [{u'word': u'sst', u'weight': 1.0}, {u'word': u'ocean temperature', u'weight': 1.0}, {u'word': u'ghrsst', u'weight': 1.0}, {u'word': u'group high resolution sea surface temperature dataset', u'weight': 0.97}, {u'word': u'reynolds sea surface temperature', u'weight': 0.83}, {u'word': u'surface temperature', u'weight': 0.82}, {u'word': u'mur', u'weight': 0.81}, {u'word': u'caspian sea', u'weight': 0.81}, {u'word': u'sea surface temperature el nino', u'weight': 0.76}, {u'word': u'ocean tempetature', u'weight': 0.76}]}}, 
# 'time': [(u'in March 3rd, 2004', datetime.datetime(2004, 3, 3, 0, 0))]}
    