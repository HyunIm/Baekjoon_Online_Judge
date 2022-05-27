N = int(input())
data = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x:(x[0], x[1]))
for i, j in data:
    print(i, j)
