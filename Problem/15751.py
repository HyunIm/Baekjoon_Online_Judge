a, b, x, y = map(int, input().split())

a2b = abs(b-a)
x2y = abs(a-x)+abs(y-b)
y2x = abs(a-y)+abs(x-b)

print(min(a2b, x2y, y2x))
