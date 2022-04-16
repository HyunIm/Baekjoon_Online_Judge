T = int(input())

for _ in range(T):
    data = sorted(list(map(int, input().split())))
    if data[3] - data[1] >= 4:
        print('KIN')
    else:
        print(sum(data[1:4]))
