from collections import deque

n = int(input())
A = list(map(int, input().split()))

que = deque()
cnt = 0
for a in A:
    last = que[-1] if que else []
    if last != [] and last[0] == a:
        if last[1] == a - 1:
            que.pop()
            cnt -= a - 1
        else:
            que[-1][1] += 1
            cnt += 1
    else:
        que.append([a, 1])
        cnt += 1
    print(cnt)
