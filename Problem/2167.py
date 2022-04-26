N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
target = [list(map(int, input().split())) for _ in range(K)]

for idx in range(K):
    i, j, x, y = target[idx]
    answer = 0
    for a in range(i-1, x):
        for b in range(j-1, y):
            answer += data[a][b]
    print(answer)
