numbers = [int(input()) for _ in range(7)]
oddNumbers = [x for x in numbers if x%2]

if len(oddNumbers) == 0:
    print(-1)
else:
    print(sum(oddNumbers))
    print(min(oddNumbers))
