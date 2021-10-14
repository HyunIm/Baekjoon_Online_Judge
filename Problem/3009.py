# File : 3009.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-10-14
# Brief : 수학

a = [list(map(int, input().split())) for _ in range(3)]
print(a[0][0] if a[1][0] == a[2][0] else a[1][0] if a[0][0] == a[2][0] else a[2][0], a[0][1] if a[1][1] == a[2][1] else a[1][1] if a[0][1] == a[2][1] else a[2][1])
