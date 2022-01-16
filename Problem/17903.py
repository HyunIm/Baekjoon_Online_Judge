m, n = map(int, input().split())
instances = [list(map(int, input().split())) for _ in range(m)]

print('satisfactory' if m >= 8 else 'unsatisfactory')
