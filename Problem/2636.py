# File : 2636.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-11-09
# Brief : BFS

from collections import deque


def meltingCheese():
    q = deque()
    q.append((0, 0))
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    leftoverCheese = 0

    while q:
        x, y = q.popleft()

        for i, j in ((0,1), (1,0), (0,-1), (-1,0)):
            nx = x + i; ny = y + j
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                visited[nx][ny] = True
                if cheese[nx][ny] == 0:
                    q.append((nx, ny))
                else:
                    cheese[nx][ny] = 0
                    leftoverCheese += 1

    meltingHistory.append(leftoverCheese)
    return leftoverCheese


n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(n)]
meltingTime = 0
meltingHistory = []

while True:
    meltingTime += 1
    lastLeftoverCheese = meltingCheese()
    if lastLeftoverCheese == 0:
        break

print(meltingTime-1)
print(meltingHistory[-2])
