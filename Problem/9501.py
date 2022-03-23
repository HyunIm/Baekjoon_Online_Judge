T = int(input())
for _ in range(T):
    N, D = map(int, input().split())
    spaceShip = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for v, f, c in spaceShip:
        if v * f / c >= D:
            result += 1
    print(result)
