n = int(input())

dp = [[-1] * 5 for _ in range(n + 1)]
dp[0][0] = 0

cur_time = 0
for i in range(1, n + 1):
    t, x, a = map(int, input().split())

    for end in range(5):
        for start in range(5):
            if dp[i - 1][start] == -1:
                continue
            dist = abs(end - start)
            # その出現場にいくのが間に合うか
            if t - cur_time >= dist:
                # そこにすぬけが出現するか
                if end == x:
                    dp[i][end] = max(dp[i][end], dp[i - 1][start] + a)
                else:
                    dp[i][end] = max(dp[i][end], dp[i - 1][start])
            else:
                # 届かないなら何もできない
                pass
    cur_time = t
print(max(dp[-1]))
