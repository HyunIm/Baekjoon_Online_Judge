# File : 1297.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-12-06
# Brief : 수학

import math

d, h, w = map(int, input().split())
diagonal = math.sqrt(h*h + w*w)
height = int(h * d / diagonal)
width = int(w * d / diagonal)
print(height, width)
