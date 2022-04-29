data = sorted(list(map(int, input().split())))
i = 0
flag = 0

while flag < 3:
    i += 1
    flag = 0
    for j in data:
        if i % j == 0:
            flag += 1

print(i)
