def notation_convert(n, base):
    T = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    q, r = divmod(n, base)
    return notation_convert(q, base) + T[r] if q else T[r]


N, B = map(int, input().split())
print(notation_convert(N, B))
