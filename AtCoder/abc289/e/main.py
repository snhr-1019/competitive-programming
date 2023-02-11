from collections import deque

t = int(input())


def solve():
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    edges = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        edges[u].append(v)
        edges[v].append(u)

    ## bfs
    d = [[-1] * n for _ in range(n)]
    d[0][n - 1] = 0
    que = deque()
    que.append((0, n - 1))

    while que:
        cur = que.pop()
        t_cur = cur[0]
        a_cur = cur[1]

        for t_nxt in edges[t_cur]:
            for a_nxt in edges[a_cur]:
                # 高橋と青木が違う色でまだ行ったことがなければ進む
                if c[t_nxt] != c[a_nxt] and d[t_nxt][a_nxt] == -1:
                    que.append((t_nxt, a_nxt))
                    d[t_nxt][a_nxt] = d[t_cur][a_cur] + 1
    print(d[n - 1][0])


for _ in range(t):
    solve()
