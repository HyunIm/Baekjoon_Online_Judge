N, W, H, L = map(int, input().split())

maxCow = ((W//L) * (H//L))

print(min(N, maxCow))
