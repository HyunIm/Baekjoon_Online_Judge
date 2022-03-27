T = int(input())
for _ in range(T):
    n = int(input())
    result = [False] * (n+1)

    for i in range(1, n+1):
        for j in range(i, n+1, i):
            result[j] = False if result[j] else True
    print(result.count(True))
