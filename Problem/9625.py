m = {0:0, 1:1, 2:1, 3:2, 4:3}

def fibo(n):
    if not n in m:
        m[n] = fibo(n-1) + fibo(n-2)
    return m[n]

K = int(input())
fibo(K)
print(m[K-1], m[K])
