# Created in Python 3.6.5
# Justin Goldstein
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
