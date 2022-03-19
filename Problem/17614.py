N = int(input())
clap = 0

for i in range(1, N+1):
    i = str(i)
    clap += i.count('3') + i.count('6') + i.count('9')

print(clap)
