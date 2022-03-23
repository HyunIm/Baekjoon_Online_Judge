aAtk, aLife = map(int, input().split())
bAtk, bLife = map(int, input().split())

while aLife > 0 and bLife > 0:
    aLife -= bAtk
    bLife -= aAtk

if aLife <= 0 and bLife <= 0:
    print('DRAW')
elif aLife <= 0:
    print('PLAYER B')
elif bLife <= 0:
    print('PLAYER A')
