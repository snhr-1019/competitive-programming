from collections import deque


def rotate(n):
    return int(str(n)[-1] + str(n)[:-1])


a, n = map(int, input().split())

visited = set()
que = deque()

que.append([1, 0])
if n == 1:
    print(0)
    exit()

while que:
    cur, num = que.popleft()

    if cur == n:
        print(num)
        exit()

    nxt = cur * a
    if nxt not in visited and len(str(nxt)) <= len(str(n)):
        que.append([nxt, num + 1])
        visited.add(nxt)

    if cur >= 10 and cur % 10 != 0:
        nxt = rotate(cur)
        if nxt not in visited:
            que.append([nxt, num + 1])
            visited.add(nxt)
print(-1)
