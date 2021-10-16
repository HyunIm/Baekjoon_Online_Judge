# File : 4153.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-10-16
# Brief : 수학

while True:
    n = list(map(int, input().split()))
    if sum(n) == 0:
        break

    a = max(n)
    b = min(n)
    c = sum(n)-a-b

    print('right' if a**2 == b**2+c**2 else 'wrong')
