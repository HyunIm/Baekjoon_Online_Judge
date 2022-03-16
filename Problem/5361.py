price = (350.34, 230.90, 190.55, 125.30, 180.90)

testCase = int(input())

for _ in range(testCase):
    A, B, C, D, E = map(float, input().split())
    part = [A, B, C, D, E]
    cost = 0

    for i in range(5):
        cost += part[i] * price[i]
    print('$%.2f'%cost)
