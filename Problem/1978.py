# File : 1978.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-09-09
# Brief : 수학

def f(x):
    if x==1: return False
    for i in range(2, x):
        if x%i==0: return False
    return True

n = int(input())
a = list(map(int, input().split()))
r = 0
for i in a:
    if f(i): r+=1
print(r)
