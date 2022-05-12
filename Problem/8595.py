n = int(input())
data = input()
sum = 0
tmp = '0'

for i in data:
    if '0' <= i <= '9':
        tmp += i
    else:
        sum += int(tmp)
        tmp = '0'
sum += int(tmp)  
print(sum)
