table = [list(map(int, input().split())) for _ in range(9)]
maxValue = 0 
row = 0
column = 0

for i in range(9):
    for j in range(9):
        if maxValue < table[i][j]:
            maxValue = table[i][j]
            column = i
            row = j

print(maxValue)
print(column+1, row+1)
