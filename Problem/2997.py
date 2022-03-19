a, b, c = sorted(map(int, input().split()))

if c-b == b-a:
    print(c+b-a)
elif c-b == 2 * (b-a):
    print(c-(b-a))
elif 2 * (c-b) == b-a:
    print(a+(c-b))
