T = int(input())
for _ in range(T):
    N = input()
    sum_value = str(int(N) + int(N[::-1]))
    if sum_value == sum_value[::-1]:
        print('YES')
    else:
        print('NO')
