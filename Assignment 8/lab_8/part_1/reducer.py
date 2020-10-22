#!/usr/bin/env python


import sys


current_word=None 
current_count=0


lines = sys.stdin.readlines()
lines.sort()

for line in lines:    

    line=line.strip().split()

    print '%s' % (line[0])
