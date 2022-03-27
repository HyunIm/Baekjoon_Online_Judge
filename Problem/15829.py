L = int(input())
value = input()
result = 0

for i in range(L):
    num = ord(value[i]) - ord('a') + 1
    result += num * (31**i)

print(result % 1234567891)
