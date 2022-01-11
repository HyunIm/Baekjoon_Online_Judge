br, bc = map(int, input().split())
dr, dc = map(int, input().split())
jr, jc = map(int, input().split())

bessie = max(abs(jr-br), abs(jc-bc))
daisy = abs(jr-dr) + abs(jc-dc)

if bessie < daisy:
    print('bessie')
elif bessie > daisy:
    print('daisy')
else:
    print('tie')
