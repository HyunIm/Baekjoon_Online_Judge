bowl = input()
result = 10

for i in range(1, len(bowl)):
    if bowl[i] == bowl[i-1]:
        result += 5
    else:
        result += 10

print(result)
