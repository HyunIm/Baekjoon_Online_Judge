price = []
X, Y = map(int, input().split())
N = int(input())

minPrice = 100000
price.append((X, Y))

for _ in range(N):
    X, Y = map(int, input().split())
    price.append((X, Y))

for x, y in price:
    tmpPrice = 1000 * x / y
    minPrice = min(minPrice, tmpPrice)

print(minPrice)
