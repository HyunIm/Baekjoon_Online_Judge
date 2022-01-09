def main():
    ca, ba, pa = map(int, input().split())
    cr, br, pr = map(int, input().split())
    
    notReceivePassengers = 0
    notReceivePassengers += notReceiveNumber(ca, cr)
    notReceivePassengers += notReceiveNumber(ba, br)
    notReceivePassengers += notReceiveNumber(pa, pr)

    print(notReceivePassengers)


def notReceiveNumber(a, r):
    if a < r:
        return r - a
    else:
        return 0


if __name__ == '__main__':
    main()
