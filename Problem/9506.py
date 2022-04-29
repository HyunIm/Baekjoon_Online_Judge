def get_divisor(n):
    divisor = []
    for i in range(1, n):
        if n % i == 0:
            divisor.append(i)
    return divisor
            

n = int(input())
while n != -1:
    divisor = get_divisor(n)
    if n == sum(divisor):
        print(n, '= ', end='')
        print(*divisor, sep=' + ')
    else:
        print(n, 'is NOT perfect.')
    n = int(input())
