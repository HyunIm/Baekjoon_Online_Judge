A, B, C = map(int, input().split())
list = [A, B, C]

oneCount = list.count(1)
twoCount = list.count(2)

print(1 if oneCount > twoCount else 2)
