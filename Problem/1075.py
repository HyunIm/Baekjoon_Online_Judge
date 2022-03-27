N = int(input())
F = int(input())
result = 0
length = N//100*100

for i in range(length, length+101):
    if i % F == 0:
        result = i % 100
        break

print(format(result, '02'))
