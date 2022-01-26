x, y = map(int, input().split())
r = int(input())

for i, j in ((r, r), (r, -r), (-r, -r), (-r, r)):
    print(x+i, y+j)
