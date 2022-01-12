number = [int(input()) for _ in range(4)]

if number[0]>=8 and number[3]>=8 and number[1]==number[2]:
    print('ignore')
else:
    print('answer')
