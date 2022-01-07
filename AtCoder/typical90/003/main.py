from collections import deque

n = int(input())
path = [[] for _ in range(n)]

for i in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    path[a].append(b)
    path[b].append(a)


def search_farthest(start):
    dist = [-1] * n
    dist[start] = 0
    que = deque()
    que.append(start)
    farthest_index = -1
    farthest_dist = -1
    while que:
        cur = que.popleft()
        for nxt in path[cur]:
            if dist[nxt] == -1:
                que.append(nxt)
                dist[nxt] = dist[cur] + 1
                farthest_index = nxt
                farthest_dist = dist[nxt]
    return [farthest_index, farthest_dist]


index, dist = search_farthest(0)
index, dist = search_farthest(index)

print(dist + 1)
