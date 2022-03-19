for _ in range(3):
    N = int(input())
    number = [int(input()) for _ in range(N)]
    number = sum(number)
    if number == 0:
        print(0)
    elif number > 0:
        print('+')
    elif number < 0:
        print('-')
