# File : 2845.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-10-23
# Brief : 수학

l, p = map(int, input().split())
a = list(map(int, input().split()))
t = l*p
for i in a: print(i-t, end=' ')
