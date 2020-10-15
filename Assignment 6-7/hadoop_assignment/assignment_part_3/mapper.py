#!/usr/bin/python

"""mapper.py"""

import sys

def euclidean(point_a, point_b):
        
        distance = 0
        for pts1, pts2 in zip(point_a, point_b):
            distance += (pts1-pts2)**2
        
        distance = distance**0.5
        return distance




def main():

  
  cand_1 = ['5.8','4.0','1.2','0.2','Iris-setosa']
  cand_2 = ['6.1','2.8','4.0','1.3','Iris-versicolor']
  cand_3 = ['6.3','2.7','4.9','1.8','Iris-virginica']
  
  with open('iris.txt', 'r') as file: 
       data = file.readlines() 
       for line in data: 
           #line = line.strip() 
           words=line.split(",")
           #print((float(words[0]),float(words[1])))
           dist_1 = euclidean([float(words[0]),float(words[1])],[float(cand_1[0]),float(cand_1[1])])
           dist_2 = euclidean([float(words[0]),float(words[1])],[float(cand_2[0]),float(cand_2[1])])
           dist_3 = euclidean([float(words[0]),float(words[1])],[float(cand_3[0]),float(cand_3[1])])
            
           min_dist = min(dist_1,min(dist_2,dist_3))
           if min_dist == dist_1:
               print '([%s\t,%s\t,%s],\t%s)' % (words[0],words[1],'C1',1)
           elif min_dist == dist_2:
               print '([%s\t,%s\t,%s],\t%s)' % (words[0],words[1],'C2',1)
           else:
               print '([%s\t,%s\t,%s],\t%s)' % (words[0],words[1],'C3',1)


if __name__ == "__main__":
    main()







