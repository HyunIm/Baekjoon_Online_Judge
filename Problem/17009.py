apple3 = int(input())
apple2 = int(input())
apple1 = int(input())
banana3 = int(input())
banana2 = int(input())
banana1 = int(input())

totalApple = apple3*3 + apple2*2 + apple1
totalBanana = banana3*3 + banana2*2 + banana1

if totalApple > totalBanana:
    print('A')
elif totalApple < totalBanana:
    print('B')
else:
    print('T')
