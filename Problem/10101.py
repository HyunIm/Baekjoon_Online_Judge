def main():
    a, b, c = sorted([int(input()) for _ in range(3)])
    if a == b == c == 60:
        print('Equilateral')
    elif a + b + c != 180:
        print('Error')
    elif a == b or b == c or c == a:
        print('Isosceles')
    else:
        print('Scalene')


if __name__ == '__main__':
    main()
