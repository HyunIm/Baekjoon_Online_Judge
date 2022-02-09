def firstDelivery(x):
    x //= 1000
    
    if x <= 5:
        return 400
    elif 5 < x <= 10:
        return 700
    elif 10 < x <= 20:
        return 1200
    elif 20 < x <= 30:
        return 1700
    elif 30 < x:
        return x * 57


def secondDelivery(x):
    x //= 1000
    
    if x <= 2:
        return 90 + x*90
    elif 2 < x <= 5:
        return 100 + x*85
    elif 5 < x <= 20:
        return 125 + x*80
    elif 20 < x <= 40:
        return 325 + x*70
    elif 40 < x:
        return 925 + x*55


distance = list(map(int, input().split()))

firstPrice = min(firstDelivery(distance[0]), secondDelivery(distance[0]))
secondPrice = min(firstDelivery(distance[1]), secondDelivery(distance[1]))

totalPrice = firstPrice + secondPrice

print(totalPrice/100)
