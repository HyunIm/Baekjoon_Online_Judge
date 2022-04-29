N = int(input())
data = [i for i in range(1, N + 1)]
answer = []

while data:
    answer.append(data.pop(0))
    if data:
        data.append(data.pop(0))

print(*answer)
