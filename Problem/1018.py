N, M = map(int, input().split())
data = [list(input()) for _ in range(N)]
result = []

for i in range(N - 7):
    for j in range(M - 7):
        tmp1 = 0
        tmp2 = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if (x + y) % 2:
                    if data[x][y] == 'B':
                        tmp1 += 1
                    elif data[x][y] == 'W':
                        tmp2 += 1
                else:
                    if data[x][y] == 'W':
                        tmp1 += 1
                    elif data[x][y] == 'B':
                        tmp2 += 1
        result.append(tmp1)
        result.append(tmp2)

print(min(result))
