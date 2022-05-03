N = int(input())
data = [list(input()) for _ in range(N)]
K = int(input())

if K == 1:
    for i in data:
        print(*i, sep='')
elif K == 2:
    for i in data:
        print(*i[::-1], sep='')
elif K == 3:
    for i in data[::-1]:
        print(*i, sep='')
