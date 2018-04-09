# -*- coding: utf-8 -*-
"""
Author: Yongyao
Description: implement tempora parsing with dateparser package
"""

import dateparser
from dateparser.search import search_dates

print dateparser.parse('12/12/12')
# 2012-12-12 00:00:00
print dateparser.parse('1 hour ago')
# 2018-04-09 16:49:18.595631
print search_dates("ocean wind in March 3rd, 2004")
# (u'in March 3rd, 2004', datetime.datetime(2004, 3, 3, 0, 0))]

