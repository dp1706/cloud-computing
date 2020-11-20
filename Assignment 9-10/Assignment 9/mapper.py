#!/usr/bin/python3
"""
mapper.py
"""

import sys
import numpy as np

def euclidean_distance(point1, point2):
  distance = np.linalg.norm(point1 - point2)
  return distance
 
def closest_centroid(sample, centroids):
  dist = [euclidean_distance(sample, point) for point in centroids]
  closest_idx = np.argmin(dist)
  return closest_idx

centroids = np.empty(shape=(2, 6))
index = 0
with open("centroids.txt") as file:
    for line in file:
        line = line.strip()
        line = line.split(",")
        line = np.array(line, dtype=float)
        centroids[index] = line
        index += 1 

for line in sys.stdin:
    line = line.strip().split(',')
    age, fnlwgt, education_num, capital_gain, capital_loss, hpw  = float(line[0]), float(line[2]), float(line[4]), float(line[10]), float(line[11]), float(line[12])
    idx = closest_centroid([age, fnlwgt, education_num, capital_gain, capital_loss, hpw], centroids)
    print(f"{idx}, ({age, fnlwgt, education_num, capital_gain, capital_loss, hpw}, 1)")
