n = int(input())
data = list(map(int, input().split()))
answer = []

for i in range(n):
    answer.insert(data[i], i+1)
answer.reverse()

print(*answer)
