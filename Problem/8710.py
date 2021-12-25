import math


def main():
    k, w, m = map(int, input().split())
    result = math.ceil((w - k) / m)
    print(result)


if __name__ == '__main__':
    main()