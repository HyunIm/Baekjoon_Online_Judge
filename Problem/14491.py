T = int(input())
base9 = ''

while T:
    base9 += str(T % 9)
    T //= 9

print(base9[::-1])
