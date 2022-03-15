import math

N, W, H = map(int, input().split())
matches = [int(input()) for _ in range(N)]

maxLength = int(math.sqrt(W**2 + H**2))

for match in matches:
    if match <= maxLength:
        print('DA')
    else:
        print('NE')
