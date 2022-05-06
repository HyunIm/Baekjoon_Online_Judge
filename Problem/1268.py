n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
student = [[False] * n for _ in range(n)]

for i in range(5):
    for j in range(n):
        for k in range(j + 1, n):
            if data[j][i] == data[k][i]:
                student[k][j] = True
                student[j][k] = True

cnt = []
for i in student:
    cnt.append(i.count(True))

print(cnt.index(max(cnt)) + 1)
