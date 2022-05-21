T = int(input())
for _ in range(T):
    a, b = input().split()
    tmp = int(a, 2) + int(b, 2)
    print(bin(tmp)[2:])
