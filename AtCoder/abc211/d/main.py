from collections import defaultdict, deque

n, m = map(int, input().split())
graph = defaultdict(lambda: [])
queue = deque()

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue.append(1)
cnt = [0] * (n + 1)
cnt[1] = 1
dist = [-1] * (n + 1)
dist[1] = 0

while queue:
    now = queue.popleft()
    for i in graph[now]:
        if dist[i] == -1:
            queue.append(i)
            cnt[i] += cnt[now]
            dist[i] = dist[now] + 1
        elif dist[i] == dist[now] + 1:
            cnt[i] += cnt[now]
            cnt[i] %= 10 ** 9 + 7
print(cnt[n])
