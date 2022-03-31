N = int(input())
P = list(map(int, input().split()))
answer = 0
start = P[0]

for i in range(N-1):
    if P[i] >= P[i+1]:
        start = P[i+1]
    else:
        answer = max(answer, P[i+1] - start)

print(answer)
