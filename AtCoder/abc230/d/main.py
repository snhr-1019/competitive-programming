n, d = map(int, input().split())
l = []
r = []

for i in range(n):
    t, s = map(int, input().split())
    l.append(t)  # 壁の番号から左端の場所を得られる
    r.append((s, i))  # 右端の順でソートして、壁の番号を得られる
r.sort()

latest_punch_pos = -10 ** 10
ans = 0
for i in range(n):
    nxt = r[i][1]
    if l[nxt] <= latest_punch_pos + d - 1:
        # 既に破壊済みのため、スキップ
        continue
    else:
        # 破壊できてなかったら、パンチ
        ans += 1
        latest_punch_pos = r[i][0]

print(ans)
