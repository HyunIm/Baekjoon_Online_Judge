M = int(input())
belts = [list(map(int, input().split())) for _ in range(M)]

way = 0
rotation = 1

for a, b, s in belts:
    if s == 1:
        way = 0 if way == 1 else 1
    rotation = rotation//a*b
print(way, int(rotation))
