def main():
    R, C, N = map(int, input().split())

    row = R // N + 1 if R % N else R // N
    col = C // N + 1 if C % N else C // N

    print(row * col)


if __name__ == '__main__':
    main()
