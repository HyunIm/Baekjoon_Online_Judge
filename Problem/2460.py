people = 0
maxPeople = 0

for _ in range(10):
    outPeople, inPeople = map(int, input().split())
    people -= outPeople
    people += inPeople
    maxPeople = max(maxPeople, people)

print(maxPeople)
