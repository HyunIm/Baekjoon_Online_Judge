# File : 21300.py
# Dev : LimHyun (hyunzion@gmail.com)
# Since : 2021-12-05
# Brief : 수학

beer, malt, wineProducts, carbonatedSoftDrinks, seltzer, water = map(int, input().split())
containers = [beer, malt, wineProducts, carbonatedSoftDrinks, seltzer, water]
totalRefund = sum(containers) * 5
print(totalRefund)
