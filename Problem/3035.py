R, C, ZR, ZC = map(int, input().split())
data = [list(input()) for _ in range(R)]

for i in range(R):
    for _ in range(ZR):
        for j in range(C):
            print(data[i][j] * ZC, end='')
        print()
