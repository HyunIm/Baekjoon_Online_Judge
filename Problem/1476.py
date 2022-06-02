E, S, M = map(int, input().split())
ee, ss, mm = 1, 1, 1
answer = 1

while not (ee == E and ss == S and mm == M):
    ee = ee + 1 if ee != 15 else 1
    ss = ss + 1 if ss != 28 else 1
    mm = mm + 1 if mm != 19 else 1
    answer += 1

print(answer)
