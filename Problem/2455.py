maxPeople = 0
nowPeople = 0

for _ in range(4):
    outPeople, inPeople = map(int, input().split())
    
    nowPeople -= outPeople
    nowPeople += inPeople

    maxPeople = max(maxPeople, nowPeople)

print(maxPeople)
