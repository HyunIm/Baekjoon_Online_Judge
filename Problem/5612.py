n = int(input())
m = int(input())
tunnel = [list(map(int, input().split())) for _ in range(n)]

nowCar = m
maxCar = m
for inCar, outCar in tunnel:
    nowCar += inCar
    nowCar -= outCar
    maxCar = max(maxCar, nowCar)
    if nowCar < 0:
        maxCar = 0
        break

print(maxCar)
