A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

time = 0

if A < 0:
  time += C * (-A)
  A = 0
if A == 0:
  time += D
if A < B:
  time += E * (B-A)

print(time)
