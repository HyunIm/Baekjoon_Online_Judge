N = int(input())
count = 5
flag = 7

for _ in range(1, N):
    count += flag
    flag += 3

print(count % 45678)
