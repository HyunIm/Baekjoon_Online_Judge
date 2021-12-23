def main():
    a = int(input())
    b = int(input())
    c = int(input())
    ISBN = [9, 7, 8, 0, 9, 2, 1, 4, 1, 8] + [a, b, c]
    sumISBN = 0

    for i in range(13):
        if i % 2:
            sumISBN += ISBN[i]*3
        else:
            sumISBN += ISBN[i]

    print('The 1-3-sum is', sumISBN)


if __name__ == '__main__':
    main()
