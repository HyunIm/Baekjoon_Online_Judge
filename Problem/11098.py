n = int(input())
for _ in range(n):
    p = int(input())
    data = [list(input().split()) for _ in range(p)]
    data = sorted(data, key=lambda x:-int(x[0]))
    print(data[0][1])
