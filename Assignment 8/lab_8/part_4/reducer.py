#!/usr/bin/env python

"""reducer.py"""

import sys

d={}
for line in sys.stdin:
    line = line.strip().split(',')
    word, offset = line[0], int(line[1])
    d.setdefault(word, []).append(offset)
for word, list_offset in d.items():
    print '%s,%s' % (word , list_offset)
