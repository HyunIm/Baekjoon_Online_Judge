# File : 2581.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-10-09
# Brief : 수학

def f(n):
    if n==1: return False
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

n = int(input())
m = int(input())
r = 0
min = 0

for i in range(n, m+1):
    t = f(i)
    if t:
        r += i
        if min==0: min=i

print(r, min, sep='\n') if r else print(-1)
