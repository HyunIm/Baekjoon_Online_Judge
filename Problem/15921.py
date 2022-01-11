n = int(input())

if n == 0:
    print('divide by zero')

else:
    practiceRecord = list(map(int, input().split()))
    avg = sum(practiceRecord)/n
    exp = 0
    for i in practiceRecord:
        exp += i/n

    print('%.2f'%(avg/exp))
