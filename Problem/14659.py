N = int(input())
data = list(map(int, input().split()))
answer = 0

tmp = 0
height = 0
for i in data:
    if i > height:
        height = i
        tmp = 0
    else:
        tmp += 1
    answer = max(answer, tmp)

print(answer)
