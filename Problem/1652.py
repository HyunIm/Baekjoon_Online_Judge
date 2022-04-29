N = int(input())
data = [list(input()) for _ in range(N)]
x = 0
y = 0

for i in range(N):
    x_tmp = 0
    y_tmp = 0
    for j in range(N):
        if data[i][j] == '.':
            x_tmp += 1
        elif data[i][j] == 'X':
            if x_tmp >= 2:
                x += 1
            x_tmp = 0
                
        if data[j][i] == '.':
            y_tmp += 1
        elif data[j][i] == 'X':
            if y_tmp >= 2:
                y += 1
            y_tmp = 0
    if x_tmp >= 2:
        x += 1
    if y_tmp >= 2:
        y += 1

print(x, y)
