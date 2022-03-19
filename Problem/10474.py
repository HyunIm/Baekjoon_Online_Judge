x, y = map(int, input().split())

while x != 0 or y != 0:
    print(x//y, x%y, '/', y)

    x, y = map(int, input().split())
