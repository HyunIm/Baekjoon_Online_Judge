A, B = map(int, input().split())
A5to6, B5to6 = int(str(A).replace('5', '6')), int(str(B).replace('5', '6'))
A6to5, B6to5 = int(str(A).replace('6', '5')), int(str(B).replace('6', '5'))

print(A6to5+B6to5, A5to6+B5to6)
