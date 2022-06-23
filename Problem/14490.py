import math

n, m = map(int, input().split(':'))
t = math.gcd(n, m)
print(n//t, ':', m//t, sep='')
