import sys

while True:
    value = sys.stdin.readline().rstrip('\n')
    if not value:
        break
    
    lower, upper, number, blank = 0, 0, 0, 0
    for i in value:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
        elif i.isdigit():
            number += 1
        elif i.isspace():
            blank += 1
    print(lower, upper, number, blank)
