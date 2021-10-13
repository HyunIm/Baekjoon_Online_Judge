# File : 1085.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-10-13
# Brief : 수학

x, y, w, h = map(int, input().split())
print(min(x, y, w-x, h-y))
