N = int(input())
paper = [[0] * 1001 for _ in range(1001)]

for k in range(1, N + 1):
    i, j, m, n = map(int, input().split())
    for x in range(i, i + m):
        for y in range(j, j + n):
            paper[x][y] = k

for i in range(1, N + 1):
    answer = 0
    for j in paper:
        answer += j.count(i)
    print(answer)
