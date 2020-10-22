#!/usr/bin/python

import sys
import re
#from nltk import word_tokenize

for line in sys.stdin:
    
    words=line.strip()
    words = re.findall("(?=[a-zA-Z0-9])[\w']+",words)

    for word in words:
       
        #word = word.lower()
        #word = re.sub(r'[^\w]','',word)
        print '%s' % (word.lower())
