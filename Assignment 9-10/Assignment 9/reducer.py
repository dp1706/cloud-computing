#!/usr/bin/env python3
"""
reducer.py
"""

import sys
import numpy as np

sum1 = np.zeros((1, 6))
cnt1 = 0
sum2 = np.zeros((1, 6))
cnt2 = 0

for line in sys.stdin:
    line = line.strip()
    cluster_idx, value = line.split(",", 1)
    value = value.replace('(', '')
    value = value.replace(')', '')
    value = value.replace(',', '')
    value = value.split(" ")
    value.pop(0)
    final_value = np.array(value, dtype=float)
    final_value.resize(6)
    if cluster_idx == '0':
        sum1 = np.add(final_value, sum1)
        cnt1 += 1
    else:
        sum2 = np.add(final_value, sum2)
        cnt2 += 1

updated_centroid_1 = np.divide(sum1, cnt1)
updated_centroid_2 = np.divide(sum2, cnt2)
updated_centroid_1 = updated_centroid_1.reshape((6,))
updated_centroid_2 = updated_centroid_2.reshape((6,))

content1 = ""
for val in updated_centroid_1:
    content1 += str(val)
    content1 += ','
content1 = content1[:-1]

content2 = ""
for val in updated_centroid_2:
    content2 += str(val)
    content2 += ','
content2 = content2[:-1]

print(content1)
print(content2)
