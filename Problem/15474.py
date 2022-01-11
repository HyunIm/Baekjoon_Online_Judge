import math

N, A, B, C, D = map(int, input().split())

xPrice = math.ceil(N/A) * B
yPrice = math.ceil(N/C) * D

print(min(xPrice, yPrice))
