T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    candies = list(map(int, input().split()))
    kid = 0
    for candy in candies:
        kid += candy // K

    print(kid)
