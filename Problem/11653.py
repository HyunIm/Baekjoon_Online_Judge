# File : 11653.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-10-09
# Brief : 수학

n = int(input())
i = 2
while n >= i:
    if n%i: i += 1
    else:
        n //= i
        print(i)
