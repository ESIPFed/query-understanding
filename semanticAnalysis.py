#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This functions is built upon the previous MUDROD project
"""

import requests

baseUrl = "http://199.26.254.151:8080/mudrod-service/SearchVocab?concept="

def expandQuery(query):
    url = baseUrl + query
    response = requests.get(url)    
    dic = response.json()
    return dic