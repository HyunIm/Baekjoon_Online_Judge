N, K = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

data.sort(key=lambda x:(-x[1], -x[2], -x[3]))

for i in range(N):
    if data[i][0] == K:
        tmp = i

for i in range(N):
    if data[tmp][1:] == data[i][1:]:
        print(i + 1)
        break
