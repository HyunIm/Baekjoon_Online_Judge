TestCase = int(input())

for _ in range(TestCase):
    d = int(input())
    for t in range(101):
        if d < t**2 + t:
            break
    print(t - 1)
