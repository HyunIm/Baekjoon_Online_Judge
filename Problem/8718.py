def main():
    x, k = map(int, input().split())
    # 1 : 2 : 4 Ratio
    if k*7 <= x:
        print(k*7000)
    elif k*3.5 <= x:
        print(k*3500)
    elif k*1.75 <= x:
        print(k*1750)
    else:
        print(0)


if __name__ == '__main__':
    main()
