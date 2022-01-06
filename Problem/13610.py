def main():
    X, Y = map(int, input().split())
    lap = 1

    while True:
        if (Y - X) * lap >= Y:
            break
        lap += 1

    print(lap)


if __name__ == '__main__':
    main()
