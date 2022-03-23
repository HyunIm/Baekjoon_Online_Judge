def T(n):
    return n*(n+1)//2

def W(n):
    value = 0
    for k in range(1, n+1):
        value += k*T(k+1)
    return value

testCase = int(input())
for _ in range(testCase):
    n = int(input())
    print(W(n))
