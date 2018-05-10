# Created in Python 3.6.5
# Justin Goldstein
# May 10, 2018
# adapted from
'''
https://stackoverflow.com/questions/12965203/how-to-get-json-from-webpage-into-python-script
'''

import urllib.request, json 
with urllib.request.urlopen("http://199.26.254.151:8080/mudrod-service/SearchVocab?concept=sst") as url:
    data = json.loads(url.read().decode())
    print(json.dumps(data, indent=4))
