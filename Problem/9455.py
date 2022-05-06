t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(m)]
    answer = 0

    for i in range(m):
        for j in range(n):
            if data[i][j] == 1:
                for k in range(i + 1, m):
                    if data[k][j] == 0:
                        answer += 1
    print(answer)
