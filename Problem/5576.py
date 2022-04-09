W = sorted([int(input()) for _ in range(10)], reverse=True)
K = sorted([int(input()) for _ in range(10)], reverse=True)

print(sum(W[:3]), sum(K[:3]))
