# File : 1931.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-29
# Brief : 그리디

n = int(input())
a = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x:(x[1], x[0]))
c = e = 0
for i, j in a:
    if i >= e:
        e = j
        c += 1
print(c)
