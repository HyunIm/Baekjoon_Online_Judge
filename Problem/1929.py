# File : 1929.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-10-10
# Brief : 수학

m, n = map(int, input().split())
a = [True] * (n+1)
for i in range(2, n+1):
    for j in range(i+i, n+1, i):
        a[j] = False
m = 2 if m==1 else m
for i in range(m, n+1):
    if a[i]: print(i)
