# File : 5585.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-05-20
# Brief : 그리디 알고리즘

n = 1000 - (int(input()))
coin_type = [500, 100, 50, 10, 5, 1]
cnt = 0

for coin in coin_type:
    cnt += n // coin
    n %= coin

print(cnt)
