chess = [list(input()) for _ in range(8)]
result = 0
for i in range(8):
    for j in range(8):
        if (i%2 and j%2) or (i%2==0 and j%2==0):
            if chess[i][j] == 'F':
                result += 1
print(result)
