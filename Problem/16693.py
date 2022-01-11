import math

a, p1 = map(int, input().split())
r, p2 = map(int, input().split())

whole = a / p1
slice = (math.pi*(r**2)) / p2

if whole > slice:
    print('Slice of pizza')
else:
    print('Whole pizza')
