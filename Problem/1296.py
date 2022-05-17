name = input()
N = int(input())
team = sorted([input() for _ in range(N)])
tmp = []

for i in team:
    L = name.count('L') + i.count('L')
    O = name.count('O') + i.count('O')
    V = name.count('V') + i.count('V')
    E = name.count('E') + i.count('E')
    tmp.append(((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E) % 100))

print(team[tmp.index(max(tmp))])
