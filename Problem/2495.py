for _ in range(3):
    data = list(map(int, input()))
    answer = 0
    tmp = 1
    for i in range(1, 8):
        if data[i] == data[i-1]:
            tmp += 1
        else:
            answer = max(answer, tmp)
            tmp = 1
    answer = max(answer, tmp)
    print(answer)
