n = int(input())
a = list(map(lambda x: int(x) - 1, input().split()))

cur = 0
visited = [False] * n
visited[0] = True
while True:
    nxt = a[cur]
    if visited[nxt]:
        start = nxt
        end = cur
        ans = []
        while True:
            nxt = a[cur]
            ans.append(nxt + 1)
            if nxt == end:
                print(len(ans))
                print(*ans)
                exit()
            cur = nxt
    cur = nxt
    visited[cur] = True
