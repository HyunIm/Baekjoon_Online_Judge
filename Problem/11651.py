N = int(input())
data = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x:(x[1], x[0]))
for i in data:
    print(*i)
