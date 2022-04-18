N, M = map(int, input().split())
bucket = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    bucket[i], bucket[j] = bucket[j], bucket[i]

print(*bucket)
