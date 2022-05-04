def multi(n):
    value = 1
    data = list(map(int, n))
    for i in data:
        value *= i
    return value


N = input()
flag = False

for i in range(1, len(N)):
    if multi(N[:i]) == multi(N[i:]):
        print('YES')
        flag = True
        break

if flag == False:
    print('NO')
