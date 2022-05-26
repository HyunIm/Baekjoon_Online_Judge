N = int(input())
d = sorted(set([input() for _ in range(N)]), key=lambda x:(len(x), x))
print(*d, sep='\n')
