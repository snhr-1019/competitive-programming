n, k = map(int, input().split())
p = [int(i) - 1 for i in input().split()]
c = [int(i) for i in input().split()]

checked = [False] * n

ans = -10 ** 10
for i in range(n):
    if checked[i]:
        continue
    loop = []
    nxt = i
    while not checked[nxt]:
        checked[nxt] = True
        loop.append(c[nxt])
        nxt = p[nxt]

    L = len(loop)

    for start in range(L):
        s = 0
        dist = 0
        for end in range(start+1, start+L):
            dist += 1
            end %= L
            s += loop[end]
            ans = max(ans, s + max(0, sum(loop) * (k - dist) // L))

print(ans)
