n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
area = [[0]*100 for _ in range(100)]
answer = 0

for i, j in data:
    for x in range(i, i+10):
        for y in range(j, j+10):
            area[x][y] = 1

for i in area:
    answer += sum(i)
print(answer)
