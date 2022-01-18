import math

w, h = map(int, input().split())

diagonal = math.sqrt(w**2 + h**2)

print((w+h) - diagonal)
