# File : 14502.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-13
# Brief : DFS/BFS

import sys
input = sys.stdin.readline

def infect(x, y):
    for i, j in ((0,1), (1,0), (0,-1), (-1,0)):
        dx = x+i
        dy = y+j
        if 0<=dx<n and 0<=dy<m:
            if t[dx][dy]==0:
                t[dx][dy] = 2
                infect(dx, dy)

def dfs(count):
    global result

    if count == 3:
        for i in range(n):
            for j in range(m):
                t[i][j] = a[i][j]
        for i in range(n):
            for j in range(m):
                if t[i][j] == 2:
                    infect(i, j)
        c = 0
        for i in t: c += i.count(0)
        result = max(result, c)
        return

    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                a[i][j] = 1
                count += 1
                dfs(count)
                a[i][j] = 0
                count -= 1

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
t = [[0]*m for _ in range(n)]
result = 0
dfs(0)
print(result)
