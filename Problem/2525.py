def main():
    A, B = map(int, input().split())
    C = int(input())

    hour = A
    minute = B + C

    while over60minute(minute):
        minute -= 60
        hour += 1
        if over24hour(hour):
            hour = 0

    print(hour, minute)


def over60minute(minute):
    return minute >= 60


def over24hour(hour):
    return hour == 24


if __name__ == '__main__':
    main()
