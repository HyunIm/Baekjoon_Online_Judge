for _ in range(3):
    yut = list(map(int, input().split()))
    
    sumYut = sum(yut)
    
    if sumYut == 3:
        print('A')
    elif sumYut == 2:
        print('B')
    elif sumYut == 1:
        print('C')
    elif sumYut == 0:
        print('D')
    elif sumYut == 4:
        print('E')
