# File : 11047.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-27
# Brief : 그리디

n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
c = 0
for i in reversed(a):
    c += k//i
    k %= i
print(c)
