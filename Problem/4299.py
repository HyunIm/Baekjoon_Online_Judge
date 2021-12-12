def main():
    sumScore, diffScore = map(int, input().split())

    highScore, lowScore = calcScores(sumScore, diffScore)

    if noSuchScores(sumScore, diffScore, highScore, lowScore):
        print(-1)
    else:
        print(highScore, lowScore)


def noSuchScores(sumScore, diffScore, highScore, lowScore):
    if sumScore < diffScore:
        return True
    if sumScore != highScore + lowScore:
        return True
    if diffScore != highScore - lowScore:
        return True
    else:
        return False


def calcScores(sumScore, diffScore):
    highScore = (sumScore + diffScore) // 2
    lowScore = (sumScore - diffScore) // 2
    return highScore, lowScore


if __name__ == '__main__':
    main()
