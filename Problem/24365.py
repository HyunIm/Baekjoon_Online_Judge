A, B, C = map(int, input().split())

avg = (A+B+C) // 3

count = (C-avg)*2 + B-avg

print(count)
