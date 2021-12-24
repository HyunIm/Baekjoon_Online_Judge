def main():
    row, column = map(int, input().split())
    diff = min(row, column) if row%2 and column%2 else 0
    print(diff)


if __name__ == '__main__':
    main()
