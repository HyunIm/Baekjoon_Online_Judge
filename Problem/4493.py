t = int(input())

for _ in range(t):
    n = int(input())
    p1Score, p2Score = 0, 0
    for _ in range(n):
        p1, p2 = input().split()
        if p1 == p2:
            pass
        elif (p1=='R' and p2=='S') or (p1=='S' and p2=='P') or (p1=='P' and p2=='R'):
            p1Score += 1
        else:
            p2Score += 1
    if p1Score == p2Score:
        print('TIE')
    elif p1Score > p2Score:
        print('Player 1')
    elif p1Score < p2Score:
        print('Player 2')
