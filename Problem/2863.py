A, B = map(int, input().split())
C, D = map(int, input().split())

fractions = [A/C+B/D, C/D+A/B, D/B+C/A, B/A+D/C]

print(fractions.index(max(fractions)))
