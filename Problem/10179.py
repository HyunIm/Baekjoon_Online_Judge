def main():
    testcaseNum = int(input())
    products = [float(input()) for _ in range(testcaseNum)]

    for product in products:
        print('$%.2f' % (product * 0.8))


if __name__ == '__main__':
    main()
