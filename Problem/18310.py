# File : 18310.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-27
# Brief : 정렬

n = int(input())
a = sorted(list(map(int, input().split())))
print(a[(n-1)//2])
