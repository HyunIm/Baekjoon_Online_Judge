def main():
    minkuk = list(map(int, input().split()))
    mansae = list(map(int ,input().split()))
    print(max(sum(minkuk), sum(mansae)))


if __name__ == '__main__':
    main()
