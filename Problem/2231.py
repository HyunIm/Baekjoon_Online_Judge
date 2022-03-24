def makeConstructor(n):
    return n + sum(list(map(int, str(n))))


N = int(input())
result = 0

for i in range(1, N):
    if N == makeConstructor(i):
        result = i
        break
print(result)
