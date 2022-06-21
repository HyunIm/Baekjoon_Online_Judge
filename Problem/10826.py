import sys
sys.setrecursionlimit(100000)

m = {0:0, 1:1, 2:1}

def fibo(n):
    if not n in m:
        m[n] = fibo(n-1) + fibo(n-2)
    return m[n]

n = int(input())
print(fibo(n))
