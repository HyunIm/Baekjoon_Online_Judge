n, h, v = map(int, input().split())

horizontal = max(h, n-h)
vertical = max(v, n-v)

print(horizontal * vertical * 4)
