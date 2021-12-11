def main():
    N = int(input())
    row = N//2
    col = N - row
    result = (row+1) * (col+1)
    print(result)


if __name__ == '__main__':
    main()
