N, K = map(int, input().split())
students = [list(map(int, input().split())) for _ in range(N)]
room = [[0]*2 for _ in range(7)]
result = 0 

for S, Y in students:
    if room[Y][S] == 0 or room[Y][S] == K:
        room[Y][S] = 1
        result += 1
    else:
        room[Y][S] += 1

print(result)
