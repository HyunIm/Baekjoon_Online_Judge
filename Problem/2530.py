def main():
    A, B, C = map(int, input().split())
    D = int(input())

    hour = A
    minute = B
    second = C + D

    while over60second(second):
        second -= 60
        minute += 1
        if over60minute(minute):
            minute -= 60
            hour += 1
            if over24hour(hour):
                hour = 0

    print(hour, minute, second)


def over60second(second):
    return second >= 60


def over60minute(minute):
    return minute >= 60


def over24hour(hour):
    return hour == 24


if __name__ == '__main__':
    main()
