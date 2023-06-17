n = int(input())
dp = [[-1] * 2 for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    xi, yi = map(int, input().split())
    if xi == 0:  # 解毒剤入りの料理の場合
        # 元が解毒状態の場合、食べても食べなくても、解毒状態のまま
        if dp[i][0] != -1:
            dp[i + 1][0] = max(dp[i + 1][0], dp[i][0] + yi)
            dp[i + 1][0] = max(dp[i + 1][0], dp[i][0])

        # 元が毒状態の場合、食べたら解毒状態になる、食べなかったら毒状態のまま
        if dp[i][1] != -1:
            dp[i + 1][0] = max(dp[i + 1][0], dp[i][1] + yi)
            dp[i + 1][1] = max(dp[i + 1][1], dp[i][1])

    else:  # 毒入りの料理の場合
        # 元が解毒状態で食べる場合、毒状態になる、食べない場合、毒状態にならない
        if dp[i][0] != -1:
            dp[i + 1][1] = max(dp[i + 1][1], dp[i][0] + yi)
            dp[i + 1][0] = max(dp[i + 1][0], dp[i][0])

        # 元が毒状態の場合、食べられない
        if dp[i][1] != -1:
            dp[i + 1][1] = max(dp[i + 1][1], dp[i][1])
print(max(dp[n]))
