# File : 1080.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-29
# Brief : 그리디

def f(i, j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            a[x][y] = 0 if a[x][y] else 1

n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]
b = [list(map(int, input())) for _ in range(n)]
c = 0
for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            c += 1
            f(i, j)
print(c if a==b else -1)

