def main():
    K, N, M = map(int, input().split())
    cookieTotalPrice = K * N
    requestPrice = cookieTotalPrice - M

    if unnecessaryPrice(requestPrice):
        requestPrice = 0

    print(requestPrice)


def unnecessaryPrice(Price):
    if Price < 0:
        return True


if __name__ == '__main__':
    main()
