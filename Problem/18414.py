X, L, R = map(int, input().split())

if L <= X <= R:
    print(X)
else:
    if abs(X-L) < abs(X-R):
        print(L)
    else:
        print(R)
