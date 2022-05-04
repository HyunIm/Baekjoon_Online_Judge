data = list(map(int, input().split()))

while data[0] != -1:
    answer = 0
    for i in data[:-1]:
        if i * 2 in data:
            answer += 1
    print(answer)

    data = list(map(int, input().split()))
