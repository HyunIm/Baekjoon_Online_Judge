# File : 17496.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-12-03
# Brief : 수학

n, t, c, p = map(int, input().split())
today = 1
count = 0
lastDay = n - t

while lastDay >= today:
    count += c
    today += t

totalPrice = count * p
print(totalPrice)
