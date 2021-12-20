def main():
    fishFinder = [int(input()) for _ in range(4)]
    result = 0
    for i in range(len(fishFinder)-1):
        if fishFinder[i] < fishFinder[i+1]:
            result += 1
        elif fishFinder[i] > fishFinder[i+1]:
            result -= 1

    if len(set(fishFinder)) == 1:
        print("Fish At Constant Depth")
    elif result == 3:
        print("Fish Rising")
    elif result == -3:
        print("Fish Diving")
    else:
        print("No Fish")


if __name__ == '__main__':
    main()
