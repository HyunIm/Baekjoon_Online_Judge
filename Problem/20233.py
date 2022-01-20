def calcFee(montlyFee, minuteFee, FreeMinute, totalTime):
    totalTime *= 21
    FreeMinute *= 21
    
    if totalTime <= FreeMinute:
        return montlyFee
    else:
        return montlyFee + (totalTime-FreeMinute)*minuteFee

a = int(input())
x = int(input())
b = int(input())
y = int(input())
T = int(input())

firstOption = calcFee(a, x, 30, T)
secondOption = calcFee(b, y, 45, T)

print(firstOption, secondOption)
