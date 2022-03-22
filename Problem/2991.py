A, B, C, D = map(int, input().split())
P, M, N = map(int, input().split())
oneDogTick, oneDogFlag = 0, True
twoDogTick, twoDogFlag = 0, True
pAtk, mAtk, nAtk = 0, 0, 0

for tick in range(1, max(P, M, N) + 1):
    if tick == P:
        if oneDogFlag:
            pAtk += 1
        if twoDogFlag:
            pAtk += 1
    if tick == M:
        if oneDogFlag:
            mAtk += 1
        if twoDogFlag:
            mAtk += 1
    if tick == N:
        if oneDogFlag:
            nAtk += 1
        if twoDogFlag:
            nAtk += 1
    
    oneDogTick += 1
    twoDogTick += 1
    if oneDogTick == A and oneDogFlag == True:
        oneDogTick = 0
        oneDogFlag = False
    elif oneDogTick == B and oneDogFlag == False:
        oneDogTick = 0
        oneDogFlag = True
    if twoDogTick == C and twoDogFlag == True:
        twoDogTick = 0
        twoDogFlag = False
    elif twoDogTick == D and twoDogFlag == False:
        twoDogTick = 0
        twoDogFlag = True

print(pAtk)
print(mAtk)
print(nAtk)
