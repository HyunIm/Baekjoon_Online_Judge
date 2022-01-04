def main():
    correctTeaType = int(input())
    answerTeaTypes = list(map(int, input().split()))
    print(answerTeaTypes.count(correctTeaType))


if __name__ == '__main__':
    main()
