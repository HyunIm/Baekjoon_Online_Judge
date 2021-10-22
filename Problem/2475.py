# File : 2475.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-10-22
# Brief : 수학

a = list(map(int, input().split()))
r = 0
for i in a: r += i*i
print(r%10)
