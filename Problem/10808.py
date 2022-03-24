S = input()
result = [0] * 26
ordA = ord('a')

for i in S:
    index = ord(i) - ordA
    result[index] += 1

print(*result)
