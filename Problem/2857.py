data = list(input() for _ in range(5))
flag = True

for i in range(5):
    if data[i].count('FBI'):
        print(i+1, end=' ')
        flag = False

if flag:
    print('HE GOT AWAY!')
