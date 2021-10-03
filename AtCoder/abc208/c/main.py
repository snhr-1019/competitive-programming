N, K = map(int, input().split())
a = list(map(int, input().split()))
rank = {v: i for i, v in enumerate(sorted(a))}
base = K // N
r = K % N

ans = []
for ai in a:
    if rank[ai] <= r:
        ans.append(base + 1)
    else:
        ans.append(base)
print(*ans)
