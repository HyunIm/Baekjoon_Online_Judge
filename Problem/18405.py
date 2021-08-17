# File : 18405.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-17
# Brief : DFS/BFS

import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

graph = []
data = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j], 0, i, j))
data.sort()
q = deque(data)

ts, tx, ty = map(int, input().split())

while q:
    v, s, x, y = q.popleft()

    if s == ts:
        break

    for i, j in ((0,1), (1,0), (0,-1), (-1,0)):
        nx = x+i; ny = y+j
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = v
                q.append((v, s+1, nx, ny))
print(graph[tx-1][ty-1])
