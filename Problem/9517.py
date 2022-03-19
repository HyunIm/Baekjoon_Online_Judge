K = int(input())
N = int(input())
questionList = [(input().split()) for _ in range(N)]
nowTime = 0

for t, z in questionList:
    nowTime += int(t)
    if nowTime >= 210:
        break

    if z == 'T':
        K = K+1 if K != 8 else 1

print(K)
