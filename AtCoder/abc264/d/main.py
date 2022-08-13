s = list(input())

at = "atcoder"
pos = {t: i for i, t in enumerate(at)}

ans = 0
for t in at:
    while True:
        ind = s.index(t)
        if pos[t] == ind:
            break
        s[ind], s[ind - 1] = s[ind - 1], s[ind]
        ans += 1
print(ans)

