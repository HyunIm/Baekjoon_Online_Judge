N = int(input())
zodiac = 'ABCDEFGHIJKL'
N = (N-4)%60
print(zodiac[N%12], N%10, sep='')
