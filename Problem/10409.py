n, T = map(int, input().split())
runTime = list(map(int, input().split()))
nowTime = 0
count = 0

for i in range(n):
    if T >= nowTime + runTime[i]:
        nowTime += runTime[i]
        count += 1
    else:
        break

print(count)
