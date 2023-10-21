from collections import deque

n, a, b, c = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1] * 2 for _ in range(n)]
dp[0][0] = 0

que = deque()
que.append((0, 0))

while que:
    cur, flag = que.popleft()
    for nxt in range(n):
        if cur == nxt:
            continue

        # 車移動中なら車のままを考慮
        if not flag:
            car_time = dp[cur][0] + d[cur][nxt] * a
            if dp[nxt][0] == -1 or car_time <= dp[nxt][0]:
                dp[nxt][0] = car_time
                que.append((nxt, 0))

        # 電車移動は必ず考慮
        train_time = dp[cur][flag] + d[cur][nxt] * b + c
        if dp[nxt][1] == -1 or train_time <= dp[nxt][1]:
            dp[nxt][1] = train_time
            que.append((nxt, 1))

print(min(dp[-1]))
