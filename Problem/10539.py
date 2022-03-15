N = int(input())
B = list(map(int, input().split()))
A = []

for i in range(N):
    A.append(B[i] * (i+1) - sum(A))

print(*A)
