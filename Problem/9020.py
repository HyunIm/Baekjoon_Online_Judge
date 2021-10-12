# File : 9020.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-10-12
# Brief : 수학

t = int(input())
a = [int(input()) for _ in range(t)]
p = [False, False] + [True] * 9999

for i in range(2, 10001):
    if p[i]:
        for j in range(2*i, 10001, i):
            p[j] = False

for i in a:
    for j in range(i//2, 1, -1):
        if p[j] and p[i-j]:
            print(j, i-j)
            break
