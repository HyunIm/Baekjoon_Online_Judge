N, M = map(int, input().split())
data = [list(input()) for _ in range(N)]
x = 0
y = 0

for i in data:
    if not 'X' in i:
        x += 1
for j in range(M):
    if not 'X' in [data[i][j] for i in range(N)]:
        y += 1
print(max(x, y))
