N, D, H = map(int, input().split())
ds = []
hs = []

for _ in range(N):
    d, h = map(int, input().split())
    ds.append(d)
    hs.append(h)

ans = 1000
for i in range(N):
    a = (H - hs[i]) / (D - ds[i])
    b = H - D * a

    ok = True
    for j in range(N):
        if a * ds[j] + b < hs[j]:
            ok = False
            break
    if ok:
        ans = min(ans, max(0, b))

print(ans)
