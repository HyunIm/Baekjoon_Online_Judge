A, B, C = map(int, input().split())
truck = [list(map(int, input().split())) for _ in range(3)]
time = max(truck[0][1], truck[1][1], truck[2][1])
answer = 0
flag = 0

for i in range(1, time+1):
    if i in (truck[0][0], truck[1][0], truck[2][0]):
        flag += [truck[0][0], truck[1][0], truck[2][0]].count(i)

    if i in (truck[0][1], truck[1][1], truck[2][1]):
        flag -= [truck[0][1], truck[1][1], truck[2][1]].count(i)

    if flag == 1:
        answer += A
    elif flag == 2:
        answer += B * 2
    elif flag == 3:
        answer += C * 3

print(answer)
