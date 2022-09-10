from collections import deque

n, m = map(int, input().split())
a = list(map(int, input().split()))

edges = [[] * (m + 1) for _ in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)


def is_ok(c):
    deleted = [False] * n
    q = deque()
    costs = [0] * n
    for i in range(n):
        for j in edges[i]:
            costs[i] += a[j]
        if costs[i] <= c:
            q.append(i)

    while q:
        # xを削除して、コストが下がったノードが削除可能になればキューに追加
        x = q.pop()
        if deleted[x]:
            continue

        for y in edges[x]:
            if not deleted[y]:
                costs[y] -= a[x]
                if costs[y] <= c:
                    q.append(y)
        deleted[x] = True

    # 全部削除できればOK
    return all(deleted)


ok = 10 ** 20
ng = -1

while ok - ng > 1:
    m = (ng + ok) // 2
    if is_ok(m):
        ok = m
    else:
        ng = m

print(ok)
