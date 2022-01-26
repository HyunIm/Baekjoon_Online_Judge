S = int(input())
A = int(input())
B = int(input())

if S <= A:
    print(250)
else:
    addHeight = S - A
    addPay = addHeight//B+1 if addHeight%B else addHeight//B
    print(250 + 100*addPay)
