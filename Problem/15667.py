N = int(input())

for k in range(N):
    if 1 + k + k**2 == N:
        break
print(k)
