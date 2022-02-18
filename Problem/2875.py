def decreaseNM(N, M):
    if N//2 == M:
        return N-1, M
    elif N//2 > M:
        return N-1, M
    else:
        return N, M-1


N, M, K = map(int, input().split())

for _ in range(K):
    N, M = decreaseNM(N, M)

print(min(N//2, M))
