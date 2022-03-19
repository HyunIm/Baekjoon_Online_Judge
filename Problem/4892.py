n0 = int(input())
index = 1

while n0 != 0:
    n1 = 3 * n0
    n1Value = 'odd' if n1%2 else 'even'

    if n1%2:
        n2 = n1 // 2
    else:
        n2 = (n1+1) // 2

    n3 = 3 * n2

    n4 = n3 // 9

    print(index, '. ', n1Value, ' ', n4, sep='')

    index += 1
    n0 = int(input())
