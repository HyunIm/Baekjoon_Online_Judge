N = int(input())
result = 2
tmp = 1

for _ in range(N):
    result += tmp
    tmp *= 2

print(result**2)
