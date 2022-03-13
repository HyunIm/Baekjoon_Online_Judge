T = int(input())

for _ in range(T):
    data = list(map(int, input().split()))
    even = [x for x in data if x%2==0]
    print(sum(even), min(even))
