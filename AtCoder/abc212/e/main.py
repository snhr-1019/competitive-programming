N, M, K = map(int, input().split())
paths = [set() for i in range(N)]
for i in range(M):
    U, V = map(int, input().split())
    U -= 1
    V -= 1
    paths[U].add(V)
    paths[V].add(U)

a = [[0] * N for i in range(K + 1)]
a[0][0] = 1
for k in range(K):
    for n in range(N):
        for nn in range(N):
            if n != nn and nn not in paths[n]:
                a[k + 1][nn] += a[k][n]
                a[k + 1][nn] %= 998244353
print(a[K][0])
