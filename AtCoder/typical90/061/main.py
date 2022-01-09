from collections import deque

q = int(input())
que = deque()
for i in range(q):
    t, x = map(int, input().split())
    if t == 1:
        que.appendleft(x)
    elif t == 2:
        que.append(x)
    else:
        print(que[x - 1])

