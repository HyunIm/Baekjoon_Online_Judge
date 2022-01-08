A, B, C, D = map(int, input().split())
teams = [A, B, C, D]

highPlayer = max(teams)
lowPlayer = min(teams)
xTeams = highPlayer + lowPlayer
yTeams = sum(teams) - xTeams

print(abs(xTeams - yTeams))
