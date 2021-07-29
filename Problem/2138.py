# File : 2138.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-07-29
# Brief : 그리디

n = int(input())
d = list(map(int, input()))
b = list(map(int, input()))
c = [0, 1]

for j in range(2):
    a = d.copy()
    for i in range(1, n):
        if a[i-1] != b[i-1]:
            c[j] += 1
            if i==n-1:
                a[n-2] = 1 - a[n-2]
                a[n-1] = 1 - a[n-1]
            else:
                for k in range(i-1, i+2):
                    a[k] = 1 - a[k]
    c[j] = c[j] if a==b else -1
    d[0] = 1 - d[0]
    d[1] = 1 - d[1]

if min(c)==-1: r=max(c)
else: r=min(c)
print(r)
