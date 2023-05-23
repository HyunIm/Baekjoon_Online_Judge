X = int(input())
N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

total_amount = sum([i * j for i, j in L])

print('Yes' if X == total_amount else 'No')
