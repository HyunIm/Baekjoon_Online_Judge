gameResults = [input() for _ in range(6)]
winCount = gameResults.count('W')
if winCount >= 5:
  print(1)
elif winCount >= 3:
  print(2)
elif winCount >= 1:
  print(1)
else:
  print(-1)
