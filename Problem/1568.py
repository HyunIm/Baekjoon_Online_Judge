N = int(input())
bird = N
song = 1
second = 0

while bird:
    second += 1
    if bird < song:
        song = 1
    bird -= song
    song += 1

print(second)
