s, k, h = map(int, input().split())
university = [s, k, h]

if sum(university) >= 100:
    print('OK')
else:
    minUniv = university.index(min(university))

    if minUniv == 0:
        print('Soongsil')
    elif minUniv == 1:
        print('Korea')
    elif minUniv == 2:
        print('Hanyang')
