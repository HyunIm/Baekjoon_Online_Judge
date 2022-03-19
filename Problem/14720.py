N = int(input())
storeList = list(map(int, input().split()))
flag = 0
milk = 0

for store in storeList:
    if store == flag:
        milk += 1
        flag = flag + 1 if flag != 2 else 0

print(milk)
