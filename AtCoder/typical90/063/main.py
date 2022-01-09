h, w = map(int, input().split())
p = []

for i in range(h):
    p.append(list(map(int, input().split())))

ans = 0
for t in range(2 ** h):
    i_list = []
    for s in range(h):
        if (t >> s) & 1:
            i_list.append(s)
    cnt = [0] * ((h + 1) * (w + 1))

    for j in range(w):
        ok = True
        for i in i_list:
            if p[i_list[0]][j] != p[i][j]:
                ok = False
                break
        if len(i_list) > 0 and ok:
            cnt[p[i_list[0]][j]] += 1
    ans = max(ans, max(cnt) * len(i_list))
print(ans)
