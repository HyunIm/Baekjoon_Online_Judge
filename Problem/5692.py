import sys
import math

def factorialBase(n):
    result = 0
    length = len(n)
    for i in (list(map(int, n))):
        result += i * math.factorial(length)
        length -= 1
    return result
        

n = sys.stdin.readline().rstrip()

while n[0] != '0':
    print(factorialBase(n))
    n = sys.stdin.readline().rstrip()
