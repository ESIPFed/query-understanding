#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 20:56:57 2018

@author: yjiang
"""

import googlemaps

def geoParse(query):
    gmaps = googlemaps.Client(key='AIzaSyACekuOv6hyB5o2dQq1mpP0Bztjx0vjTuM')
    geocode_result = gmaps.geocode('sst pacific ocean')
    return geocode_result[0]['geometry']['bounds']