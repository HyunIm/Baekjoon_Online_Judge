k = int(input())

commission = k*0.01 + 25
commission = min(max(commission, 100), 2000)

print(commission)
