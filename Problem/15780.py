N, K = map(int, input().split())
multitap = list(map(int, input().split()))
canPowerMultitap = []

for i in multitap:
    if i % 2:
        canPowerMultitap.append(i//2 + 1)
    else:
        canPowerMultitap.append(i//2)

if sum(canPowerMultitap) >= N:
    print('YES')
else:
    print('NO')
