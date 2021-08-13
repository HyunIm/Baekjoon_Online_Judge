# File : 18352.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-13
# Brief : DFS/BFS

import sys
input = sys.stdin.readline
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)

calc = [-1]*(n+1)
calc[x] = 0

q = deque([x])
while q:
    now = q.popleft()
    for i in graph[now]:
        if calc[i] == -1:
            calc[i] = calc[now] + 1
            q.append(i)

f = True
for i in range(n+1):
    if calc[i]==k:
        print(i)
        f = False

print('-1' if f else '', end='')
