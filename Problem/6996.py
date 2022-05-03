t = int(input())
for _ in range(t):
    a, b = input().split()
    ta = list(sorted(list(a)))
    tb = list(sorted(list(b)))
    print(a, '&', b, 'are ', end='')
    if ta == tb:
        print('anagrams.')
    else:
        print('NOT anagrams.')
