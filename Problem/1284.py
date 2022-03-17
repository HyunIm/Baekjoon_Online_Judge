N = list(map(int, input()))

while N[0] != 0:
    width = 1

    for i in N:
        if i == 0:
            width += 5
        elif i == 1:
            width += 3
        else:
            width += 4

    print(width)
    N = list(map(int, input()))
