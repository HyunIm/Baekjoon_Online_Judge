n = int(input())
answer = 0

for i in range(1, n+1):
    for j in range(i, n+1):
        if i*j <= n:
            answer += 1
print(answer)
