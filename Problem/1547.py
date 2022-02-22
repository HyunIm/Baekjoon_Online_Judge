M = int(input())
ballLocation = 1

for _ in range(M):
    X, Y = map(int, input().split())
    if ballLocation == X:
        ballLocation = Y
    elif ballLocation == Y:
        ballLocation = X

print(ballLocation)
