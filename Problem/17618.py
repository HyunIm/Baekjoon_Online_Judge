N = int(input())
result = 0

for i in range(1, N+1):
    if i % (sum(list(map(int, str(i))))) == 0:
        result += 1

print(result)
