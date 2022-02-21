N = int(input())
powerStrips = [int(input()) for _ in range(N)]

print(sum(powerStrips) - N + 1)
