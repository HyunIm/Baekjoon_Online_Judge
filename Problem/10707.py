def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    P = int(input())
    XCompany = A * P
    YCompany = calcYCompany(B, C, D, P)
    chargePerMonth = min(XCompany, YCompany)
    print(chargePerMonth)


def calcYCompany(B, C, D, P):
    if C >= P:
        return B
    else:
        overLiter = P - C
        overCharge = overLiter * D
        return B + overCharge


if __name__ == '__main__':
    main()
