a, b, c = sorted(map(int, input().split()))

while a != 0 or b != 0 or c != 0:
    if a + b <= c:
        print('Invalid')
    elif a == b == c:
        print('Equilateral')
    elif a == b or b == c or c == a:
        print('Isosceles')
    else:
        print('Scalene')

    a, b, c = sorted(map(int, input().split()))
