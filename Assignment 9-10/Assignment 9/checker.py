#!/usr/bin/python3
"""
checker.py
"""
import sys
import math
import numpy as np

def euclidiean_dist(x1,x2):
    x1,x2 = np.array(x1),np.array(x2)
    return math.sqrt(sum((x1-x2)**2))

def read_centroids(filename='centroids.txt'):
    fh = open(filename,'r')
    file = fh.readlines()
    centroids = np.empty(shape=(2, 6))
    index = 0
    for line in file:
        line = line.strip()
        line = line.split(",")
        line = np.array(line, dtype=float)
        centroids[index] = line
        index += 1

    return centroids

if __name__ == "__main__":

    prev_centroids = read_centroids()
    curr_centroids = read_centroids(sys.argv[1])

    for i in range(len(prev_centroids)):
        if(euclidiean_dist(prev_centroids[i],curr_centroids[i]) > 10**-6):
            print(0)
            exit(0)

    print(1)
