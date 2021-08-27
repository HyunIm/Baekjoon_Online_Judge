# File : 1715.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-27
# Brief : 정렬

import sys
input = sys.stdin.readline
import heapq
n = int(input())
q = []
r = 0
for _ in range(n):
    heapq.heappush(q, int(input()))
while len(q) != 1:
    t = heapq.heappop(q) + heapq.heappop(q)
    r += t
    heapq.heappush(q, t)
print(r)
