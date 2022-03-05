testCaseNumber = int(input())

for _ in range(testCaseNumber):
    s = int(input())
    n = int(input())
    for _ in range(n):
        q, p = map(int, input().split())
        s += q*p
    print(s)
