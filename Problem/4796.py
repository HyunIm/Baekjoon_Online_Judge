L, P, V = map(int, input().split())

i = 0
while not (L == 0 and P == 0 and V == 0):
    answer = (V//P)*L + min((V%P), L)
    i += 1
    print('Case ', i, ': ', answer, sep='')

    L, P, V = map(int, input().split())
