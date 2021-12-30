def main():
    T = int(input())

    if T % 10:
        print(-1)

    else:
        A = T // 300
        T %= 300
        B = T // 60
        T %= 60
        C = T // 10
        T %= 10

        print(A, B, C)


if __name__ == '__main__':
    main()
