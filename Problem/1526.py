def get_answer(N):
    for i in range(N, 3, -1):
        tmp = list(map(int, str(i)))
        flag = True
        for j in tmp:
            if not j in [4, 7]:
                flag = False
        if flag:
            return i


N = int(input())
print(get_answer(N))
