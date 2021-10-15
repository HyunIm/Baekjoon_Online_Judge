# File : 10870.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-10-15
# Brief : 재귀

m = {0: 0, 1: 1, 2: 1}

def f(n):
    if n in m:
        return m[n]
    else:
        m[n] = f(n-1) + f(n-2)
        return m[n]

print(f(int(input())))
