h, w, m = map(int, input().split())
h_cnt = [0] * h
w_cnt = [0] * w

bomb_list = {}

for i in range(m):
    h_, w_ = map(int, input().split())
    h_ -= 1
    w_ -= 1
    h_cnt[h_] += 1
    w_cnt[w_] += 1
    bomb_list[h_][w_] = 1

max_h = max(h_cnt)
max_h_idx = []
for i in range(h):
    if h_cnt[i] == max_h:
        max_h_idx.append(i)

max_w = max(w_cnt)
max_w_idx = []
for i in range(w):
    if w_cnt[i] == max_w:
        max_w_idx.append(i)

minus = -1
for i in max_h_idx:
    for j in max_w_idx:
        if bomb_list.get(i).get(j) != 1:
            print(max_h + max_w)
            exit()
print(max_h + max_w - 1)
