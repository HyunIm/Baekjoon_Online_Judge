fibo = {0:0, 1:1, 2:1}

def calcFibo(n):
    if n in fibo:
        return fibo[n]
    else:
        fibo[n] = calcFibo(n-1) + calcFibo(n-2)
        return fibo[n]

n = int(input())
print(calcFibo(n))
