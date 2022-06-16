n = int(input())
data = [input().split() for _ in range(n)]
company = set()

for name, do in data:
    if do == 'enter':
        company.add(name)
    elif do == 'leave':
        company.remove(name)

company.sort(reverse=True)
print(*company, sep='\n')
