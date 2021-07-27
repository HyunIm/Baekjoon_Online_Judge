# File : 1931.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-27
# Brief : 그리디

n = int(input())
a = sorted(list(map(int, input().split())))
s = 0
for i in range(1, n+1):
    s += sum(a[0:i])
print(s)
