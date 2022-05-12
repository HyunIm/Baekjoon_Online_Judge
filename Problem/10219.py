T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    meats = [input() for _ in range(H)]
    for i in meats:
        print(*i[::-1], sep='')
