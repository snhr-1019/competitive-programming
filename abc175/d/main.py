n, k = map(int, input().split())
p = [int(i) - 1 for i in input().split()]
c = [int(i) for i in input().split()]

checked = [False] * n

ans = 0
for i in range(n):
    if checked[i]:
        continue
    tmp = []
    next = i
    while not checked[next]:
        checked[next] = True
        tmp.append(c[next])
        next = p[next]

    # 最大値を求める処理
    tmp_max = k // len(tmp) * sum(tmp)
    tmp_max2 = 0
    k = k - k // len(tmp)
    for j in range(len(tmp)):
        tmp_max2 = max(sum(tmp[i:k]), tmp_max2)
    ans = max(ans, tmp_max + tmp_max2)

print(ans)
