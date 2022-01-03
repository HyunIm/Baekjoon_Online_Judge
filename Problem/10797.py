def main():
    target = int(input())
    carNumbers = list(map(int, input().split()))
    print(carNumbers.count(target))


if __name__ == '__main__':
    main()
