contestants = [list(map(int, input().split())) for _ in range(5)]

contestants = list(map(sum, contestants))

print(contestants.index(max(contestants))+1, max(contestants))
