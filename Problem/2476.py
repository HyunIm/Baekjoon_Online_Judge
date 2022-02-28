N = int(input())
maxPrice = 0

for _ in range(N):
    a, b, c = map(int, input().split())

    if a == b == c:
        price = 10000 + a * 1000
        maxPrice = max(maxPrice, price)
    elif a == b or a == c:
        price = 1000 + a * 100
        maxPrice = max(maxPrice, price)
    elif b == c:
        price = 1000 + b * 100
        maxPrice = max(maxPrice, price)
    else:
        price = max(a, b, c) * 100
        maxPrice = max(maxPrice, price)

print(maxPrice)
