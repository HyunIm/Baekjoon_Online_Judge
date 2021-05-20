# File : 5585.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-05-20
# Brief : 그리디 알고리즘

n = 1000 - (int(input()))
cnt = 0

while n > 0:
    if n >= 500:
        n -= 500
        cnt += 1
    elif n >= 100:
        n -= 100
        cnt += 1
    elif n >= 50:
        n -= 50
        cnt += 1
    elif n >= 10:
        n -= 10
        cnt += 1
    elif n >= 5:
        n -= 5
        cnt += 1
    else :
        n -= 1
        cnt += 1

print(cnt)
