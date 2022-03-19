A, B = map(int, input().split())
C = int(input())

balance = A + B

if A + B >= 2 * C:
    balance -= 2 * C

print(balance)
