n = input()

result = sum(map(int, n))
result += (len(n)-2) * 9

print(result)
