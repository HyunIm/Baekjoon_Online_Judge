def calc(x, y):
    result = 0
    while x > 0:
        result += x % y
        x //= y
    return result

for i in range(1000, 10000):
    num10 = calc(i, 10)
    num12 = calc(i, 12)
    num16 = calc(i, 16)
    if num10 == num12 == num16:
        print(i)
