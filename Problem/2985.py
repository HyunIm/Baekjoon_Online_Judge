a, b, c = input().split()
signs = ['+', '-', '*', '/']

for sign in signs:
    exp = a+sign+b
    if eval(exp) == int(c):
        print(exp+'='+c)
        break
    exp = b+sign+c
    if int(a) == eval(exp):
        print(a+'='+exp)
        break
