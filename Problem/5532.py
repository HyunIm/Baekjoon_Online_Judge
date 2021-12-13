def main():
    L, A, B, C, D = map(int, [input() for _ in range(5)])
    koreanHomeworkDay = calcHomeworkDay(A, C)
    mathHomeworkDay = calcHomeworkDay(B, D)
    print(calcFreeDay(L, koreanHomeworkDay, mathHomeworkDay))


def calcHomeworkDay(totalPages, solvePages):
    homeworkDay = totalPages // solvePages
    if totalPages % solvePages:
        homeworkDay += 1
    return homeworkDay


def calcFreeDay(L, koreanHomeworkDay, mathHomeworkDay):
    return L - max(koreanHomeworkDay, mathHomeworkDay)


if __name__ == '__main__':
    main()
