testCase = int(input())

for _ in range(testCase):
    n = int(input())

    print('Pairs for ', n, ':', sep='', end=' ')
    for i in range(1, n//2+1):
        if i != n-i:
            if i != 1:
                print(',', end=' ')
            print(i, n-i, end='')
    print()
