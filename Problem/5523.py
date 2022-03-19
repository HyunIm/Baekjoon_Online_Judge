N = int(input())
aWin, bWin = 0, 0

for _ in range(N):
    A, B = map(int, input().split())
    if A > B:
        aWin += 1
    elif A < B:
        bWin += 1

print(aWin, bWin)
