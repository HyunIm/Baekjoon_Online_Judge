N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
answer = [0] * N
round = []

for i in range(3):
    round.append([j[i] for j in data])

for i in range(3):
    for j in range(N):
        answer[j] += data[j][i] if round[i].count(data[j][i]) == 1 else 0

print(*answer, sep='\n')
