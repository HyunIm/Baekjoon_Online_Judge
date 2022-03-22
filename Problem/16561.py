n = int(input())
result = 0

for i in range(3, n, 3):
    for j in range(3, n, 3):
        for k in range(3, n, 3):
            if n == i+j+k:
                result += 1
print(result)
