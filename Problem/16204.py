N, M, K = map(int, input().split())

frontO = M
frontX = N - M
backO = K
backX = N - K

print(min(frontO, backO) + min(frontX, backX))
