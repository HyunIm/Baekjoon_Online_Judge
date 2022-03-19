num = int(input())
sign = input()
result = num

while sign != '=':
    num = int(input())
    result = int(eval(str(result) + sign + str(num)))
    sign = input()

print(result)
