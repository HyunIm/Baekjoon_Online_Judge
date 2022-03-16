def isDivisor(number, i):
    for num in number:
        if num%i != 0:
            return False
    return True

n = int(input())
number = sorted(list(map(int, input().split())))

for i in range(1, number[0]+1):
    if not isDivisor(number, i):
        continue
    print(i)
