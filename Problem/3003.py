# File : 3003.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-10-25
# Brief : 수학

a = [1, 1, 2, 2, 2, 8]
b = list(map(int, input().split()))
for i in range(6): print(a[i]-b[i], end=' ')
