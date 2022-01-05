def main():
    A, B = map(int, input().split())
    C, D = map(int, input().split())
    print(min(A+D, B+C))


if __name__ == '__main__':
    main()
