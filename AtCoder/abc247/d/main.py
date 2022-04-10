from collections import deque

q = int(input())
que = deque()

for i in range(q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        x = query[1]
        c = query[2]

        que.append([x, c])
    else:
        c = query[1]
        t = 0
        while c > 0:
            n = min(que[0][1], c)
            c -= n
            t += que[0][0] * n
            que[0][1] -= n
            if que[0][1] == 0:
                que.popleft()
        print(t)
