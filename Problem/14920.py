def C(n, i):
    if n == 1:
        return i
    else:
        if n%2:
            return C(3*n+1, i+1)
        else:
            return C(n//2, i+1)

n = int(input())
print(C(n, 1))
