N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

for i, j in data:
    tmp = 1
    for x, y in data:
        if i < x and j < y:
            tmp += 1
    print(tmp, end=' ')
