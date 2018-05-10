# Created in Python 3.6.5
# Justgo129
# May 10, 2018
# adapted from
'''
https://stackoverflow.com/questions/12965203/how-to-get-json-from-webpage-into-python-script
'''

import urllib.request, json

myUrl = "http://199.26.254.151:8080/mudrod-service/SearchVocab?concept=sst"

def parse(myUrl):
    with urllib.request.urlopen(myUrl) as url:
        data = json.loads(url.read().decode())
        print(json.dumps(data, indent=4))
        
parse(myUrl)

# output:  
# {
#    "graph": {
#        "ontology": [
#           {
#               "word": "sea surface temperature",
 #              "weight": 1.0
 #           },
 #           {
 #               "word": "ocean temperature",
 #               "weight": 1.0
 #           },
 #          {
 #               "word": "group high resolution sea surface temperature dataset",
 #               "weight": 0.89
 #         }, 
 # (etc)...
