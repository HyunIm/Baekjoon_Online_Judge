a1, a2, a3 = map(int, input().split())

while a1 != 0 or a2 != 0 or a3 != 0:
    if a3-a2 == a2-a1:
        print('AP', a3+(a2-a1))
    else:
        print('GP', a3*(a2//a1))

    a1, a2, a3 = map(int, input().split())
