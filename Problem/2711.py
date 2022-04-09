T = int(input())

for _ in range(T):
    n, data = input().split()
    data = list(data)
    del data[int(n)-1]

    print(*data, sep='')
