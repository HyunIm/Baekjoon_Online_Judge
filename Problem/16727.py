p1, s1 = map(int, input().split())
s2, p2 = map(int, input().split())

sumP = p1+p2
sumS = s1+s2

if sumP == sumS:
    if s1 == p2:
        print('Penalty')
    elif s1 < p2:
        print('Persepolis')
    else:
        print('Esteghlal')

elif sumP > sumS:
    print('Persepolis')
else:
    print('Esteghlal')
