N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
score = [0, 0, 0]
vote_list = [[] for _ in range(3)]

for i, j, k in data:
    vote_list[0].append(i)
    vote_list[1].append(j)
    vote_list[2].append(k)
for i in range(3):
    score[i] = sum(vote_list[i])
max_score = max(score)

only_max_value_flag = True if score.count(max_score) == 1 else False
if only_max_value_flag:
    print(score.index(max_score) + 1, max_score)
else:
    max_value_index_list = []
    for i in range(3):
        if score[i] == max(score):
            max_value_index_list.append(i)

    for i in range(3):
        tmp = [0] * 3
        for j in range(3):
            if j in max_value_index_list:
                tmp[j] = vote_list[j].count(3-i)
        only_max_value_flag = True if tmp.count(max(tmp)) == 1 else False
        if only_max_value_flag:
            print(tmp.index(max(tmp)) + 1, max_score)
            break

    if not only_max_value_flag:
        print(0, max_score)
