from collections import Counter

data = [int(input()) for _ in range(10)]
cnt = Counter(data)
print(sum(data)//10)
print(cnt.most_common()[0][0])
