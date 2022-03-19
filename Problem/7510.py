n = int(input())
for i in range(1, n+1):
    a, b, c = sorted(map(int, input().split()))

    print('Scenario #', i, ':', sep='')
    if a**2 + b**2 == c**2:
        print('yes')
    else:
        print('no')

    print()
