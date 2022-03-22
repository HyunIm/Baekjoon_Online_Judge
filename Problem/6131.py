N = int(input())
result = 0

for a in range(1, N+1):
    for b in range(1, a+1):
        if a**2 - b**2 == N:
            result += 1
print(result)
