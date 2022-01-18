S = int(input())
M = int(input())
L = int(input())

happinessScore = S + 2*M + 3*L
print('happy' if happinessScore >= 10 else 'sad')
