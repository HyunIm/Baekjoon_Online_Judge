T = int(input())

for _ in range(T):
    sumY = 0
    sumK = 0

    for _ in range(9):
        Y, K = map(int, input().split())
        sumY += Y
        sumK += K

    if sumY > sumK:
        print('Yonsei')
    elif sumY < sumK:
        print('Korea')
    elif sumY == sumK:
        print('Draw')
