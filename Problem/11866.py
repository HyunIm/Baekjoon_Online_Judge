N, K = map(int, input().split())
data = [i for i in range(1, N + 1)]
answer = []

while data:
    for _ in range(K-1):
        data.append(data.pop(0))
    answer.append(data.pop(0))

print('<', end='')
print(*answer, sep=', ', end='')
print('>')
