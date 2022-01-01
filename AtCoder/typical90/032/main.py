import itertools

N = int(input())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))
M = int(input())

rumor = [set() for _ in range(N)]
for i in range(M):
    x, y = map(lambda z: int(z) - 1, input().split())
    rumor[x].add(y)
    rumor[y].add(x)

ans = 10 ** 10
for v in itertools.permutations(list(range(N))):
    ng = False
    for i in range(1, N):
        if v[i] in rumor[v[i - 1]]:
            ng = True
            break
    if ng:
        continue

    t = 0
    for i in range(N):
        t += A[v[i]][i]
    ans = min(ans, t)

if ans == 10 ** 10:
    print(-1)
else:
    print(ans)
