N = int(input())
data = sorted([list(input().split()) for _ in range(N)], key=lambda x:int(x[0]))
for i in data:
    print(*i)
