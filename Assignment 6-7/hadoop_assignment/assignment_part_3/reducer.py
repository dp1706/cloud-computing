#!/usr/bin/env python

"""reducer.py"""

import sys
import re

class_1 = 'Iris-setosa'
class_2 = 'Iris-versicolor'
class_3 = 'Iris-virginica'

spel_l , spel_w , count_1 = 0.0,0.0,0
spel_l_2 , spel_w_2 , count_2 = 0.0,0.0,0
spel_l_3 , spel_w_3 , count_3 = 0.0,0.0,0


for line in sys.stdin:
   
       line = line.strip()
       line = re.sub('[^\w\s.]','',line)
       line = line.split()

       if line[2] == 'C1':
           spel_l  += float(line[0])
           spel_w  += float(line[1])
           count_1 += int(line[3])

       elif line[2] == 'C2':
           spel_l_2  += float(line[0])
           spel_w_2  += float(line[1])
           count_2 += int(line[3])

       else :
           
           spel_l_3  += float(line[0])
           spel_w_3  += float(line[1])
           count_3 += int(line[3])

             
       
##################### NEW Candidate point ###############################

spel_l , spel_w = spel_l/float(count_1) , spel_w/float(count_1)
spel_l_2 , spel_w_2 = spel_l_2/float(count_2) , spel_w_2/float(count_2)
spel_l_3 , spel_w_3 = spel_l_3/float(count_3) , spel_w_3/float(count_3)


print '[%s,%s,%s]' % (spel_l,spel_w,class_1)
print '[%s,%s,%s]' % (spel_l_2,spel_w_2,class_2)
print '[%s,%s,%s]' % (spel_l_3,spel_w_3,class_3)

   
   



