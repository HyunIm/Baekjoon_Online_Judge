# File : 1932.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-08-30
# Brief : 다이나믹 프로그래밍

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
	for j in range(i+1):
		left = 0 if j==0 else a[i-1][j-1]
		right = 0 if j==i else a[i-1][j]
		a[i][j] += max(left, right)
print(max(a[n-1]))
