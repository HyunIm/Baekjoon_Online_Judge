A = list(map(int, input().split()))
B = list(map(int, input().split()))
aScore = 0
bScore = 0
winFlag = 'D'

for i in range(10):
    if A[i] == B[i]:
        aScore += 1
        bScore += 1
    elif A[i] > B[i]:
        aScore += 3
        winFlag = 'A'
    elif A[i] < B[i]:
        bScore += 3
        winFlag = 'B'

print(aScore, bScore)
if aScore == bScore:
    print(winFlag)
elif aScore > bScore:
    print('A')
elif aScore < bScore:
    print('B')
