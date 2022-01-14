n = int(input())
remainder = n % 8

if remainder == 1:
    print(1)
elif remainder in [2, 0]:
    print(2)
elif remainder in [3, 7]:
    print(3)
elif remainder in [4, 6]:
    print(4)
else:
    print(5)
