n = list(map(int, input()))

while n[0] != 0:
    while len(n) != 1:
        n = sum(n)
        n = list(map(int, str(n)))

    print(*n)

    n = list(map(int, input()))
