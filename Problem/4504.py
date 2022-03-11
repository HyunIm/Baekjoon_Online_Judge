n = int(input())

x = int(input())
while x != 0:
    if x % n:
        print(x, ' is NOT a multiple of ', n, '.', sep='')
    else:
        print(x, ' is a multiple of ', n, '.', sep='')

    x = int(input())
