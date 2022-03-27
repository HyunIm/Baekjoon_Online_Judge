n = sorted([int(input()) for _ in range(28)])
j = 1

for i in n:
    if i != j:
        print(j)
        j += 1
    j += 1
