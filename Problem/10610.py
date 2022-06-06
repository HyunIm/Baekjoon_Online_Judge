N = sorted(input(), reverse=True)
tmp_sum = sum(list(map(int, N)))
if tmp_sum % 3 == 0 and '0' in N:
    print(*N, sep='')
else:
    print(-1)
