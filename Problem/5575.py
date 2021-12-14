def main():
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    print(*calcWorkTime(A))
    print(*calcWorkTime(B))
    print(*calcWorkTime(C))


def calcWorkTime(commuteTime):
    hour = commuteTime[3] - commuteTime[0]
    minute = commuteTime[4] - commuteTime[1]
    second = commuteTime[5] - commuteTime[2]
    if second < 0:
        minute -= 1
        second += 60
    if minute < 0:
        hour -= 1
        minute += 60
    return hour, minute, second


if __name__ == '__main__':
    main()
