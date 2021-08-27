# File : 10825.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-27
# Brief : 정렬

import sys
input = sys.stdin.readline
n = int(input())
a = sorted([input().split() for _ in range(n)], key=lambda a:(-int(a[1]), int(a[2]), -int(a[3]), a[0]))
for i in a: print(i[0])
