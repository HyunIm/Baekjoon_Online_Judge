def printJBox(j):
    if j == 1:
        print('#')
    else:
        print('#'*j)
        for _ in range(j-2):
            print('#' + 'J'*(j-2) + '#')
        print('#'*j)
    print()

testCase = int(input())
jList = [int(input()) for _ in range(testCase)]

for j in jList:
    printJBox(j)
