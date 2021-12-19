import itertools

N, M = map(int, input().split())

cord_t = [[0] * N for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    cord_t[a][b] = 1
    cord_t[b][a] = 1

cord_a = []
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    cord_a.append([a, b])

ans = False
for p in itertools.permutations(range(N), N):
    is_same = True
    for v in cord_a:
        if cord_t[p[v[0]]][p[v[1]]] == 0:
            is_same = False
    if is_same:
        print("Yes")
        exit()
print("No")
