import math

f = math.factorial

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(f(M) // (f(N) * f(M-N)))
