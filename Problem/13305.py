# File : 13305.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-29
# Brief : 그리디

n = int(input())
r = list(map(int, input().split()))
o = list(map(int, input().split()))
s = 0
m = o[0]

for i in range(n-1):
    m = o[i] if o[i] < m else m
    s += r[i]*m
print(s)
