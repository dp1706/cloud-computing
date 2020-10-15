#!/usr/bin/env python

"""reducer.py"""

import sys
import re


current_word = []
#This loop will only work when the input 
#to the script is sorted

for line in sys.stdin:

    #read line and split by comma
    #recall, we used comma as delimiter in mapper
   

    line=line.strip().split(',')
    word = line[0]
    word = re.sub('[^\w\s]','',word)
    word = word.lower()

    if word not in current_word:
       current_word.append(word)

current_word.sort()

for word in current_word:
    print '%s' % (word)

   

#spit last word
#print '%s,%s' % (current_word, current_count)
#print(word)
