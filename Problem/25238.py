a, b = map(int, input().split())
defence = a - a*b/100

print(1 if defence < 100 else 0)
