M, S, G = map(int, input().split())
A, B = map(float, input().split())
L, R = map(int, input().split())

leftWait = L / A
rightWait = R / B

leftUp = M / G
rightUp = M / S

leftTime = leftWait + leftUp
rightTime = rightWait + rightUp

if leftTime < rightTime:
    print('friskus')
else:
    print('latmask')
