A = int(input())
B = int(input())

hourHand = (A+B)%12

print(hourHand if hourHand else 12)
