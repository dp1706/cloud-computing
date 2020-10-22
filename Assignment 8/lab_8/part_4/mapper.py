#!/usr/bin/python

import sys
import re
#from nltk import word_tokenize

curr_offset = 0
next_offset = 0
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~|+-123456789'''
stop_words = ['the', 'of', 'and', 'to', 'in', 'I', 'that', 'was', 'his', 'he', 'it',
               'with', 'is', 'for', 'as', 'had', 'you', 'not', 'be', 'her', 'on', 'at',
                'by', 'which', 'have', 'or', 'from', 'this', 'him', 'but', 'all', 'she', 'they',
                'were', 'my', 'are', 'me', 'one', 'their', 'so', 'an', 'said', 'them', 'we',
                 'who', 'would', 'been', 'will', 'no', 'when', 'there', 'if']

for line in sys.stdin:
    curr_offset = next_offset
    next_offset += len(line)
    line = line.strip()
    for word in line.split(' '):
        word1 = ""
        for char in word:
            if char not in punctuations:
                word1 = word1 + char
        word1 = word1.lower()
        if word1 not in stop_words:
                print '%s,%s' % (word1,curr_offset)
