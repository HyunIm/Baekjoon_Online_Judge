def main():
    D, H, M = map(int, input().split())
    totalMinute = M - 11
    totalMinute += (H - 11) * 60
    totalMinute += (D - 11) * 60 * 24
    print(totalMinute if totalMinute >= 0 else -1)


if __name__ == '__main__':
    main()
