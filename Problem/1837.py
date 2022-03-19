def get_prime_list(n):
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False

    return [i for i in range(2, n) if sieve[i] == True]

def isGood(P, primeList):
    for i in primeList:
        if P % i == 0:
            return ('BAD ' + str(i))
    return 'GOOD'

P, K = map(int, input().split())
primeList = get_prime_list(K)

result = isGood(P, primeList)

print(result)
