V = int(input())
votes = list(input())
a = 0
b = 0

for vote in votes:
    if vote == 'A':
        a += 1
    elif vote == 'B':
        b += 1

if a == b:
    print('Tie')
elif a > b:
    print('A')
elif a < b:
    print('B')
