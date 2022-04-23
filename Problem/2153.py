def is_prime(n):
    n += 1
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False

    return True if sieve[n-1] else False


data = input()
number = 0
for i in data:
    if 'a' <= i <= 'z':
        number += ord(i) - ord('a') + 1
    elif 'A' <= i <= 'Z':
        number += ord(i) - ord('A') + 27

if is_prime(number):
    print('It is a prime word.')
else:
    print('It is not a prime word.')
