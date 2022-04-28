data = [list(map(int, input().split())) for _ in range(4)]
area = [[0]*100 for _ in range(100)]
answer = 0

for a, b, c, d in data:
    for i in range(a, c):
        for j in range(b, d):
            area[i][j] = 1

for i in area:
    answer += sum(i)
print(answer)
