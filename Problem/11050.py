import math

def fact(n):
    return math.factorial(n)


def get_binomial_coefficient(n, k):
    if 0 <= k <= n:
        return int(fact(n) / (fact(k) * fact(n-k)))
    else:
        return 0


N, K = map(int, input().split())
print(get_binomial_coefficient(N, K))
