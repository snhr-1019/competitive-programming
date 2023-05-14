INF = 10 ** 9
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

dp = [[INF] * (n + 1) for _ in range(1 << n)]

'''
dp[i][j]
i: 既に通った都市をビットで表したものの10進数表現
j: 今いる都市の番号
のときの最小コスト
'''
dp[0][0] = 0


def euclid_dist(i, j):
    return ((xy[i][0] - xy[j][0]) ** 2 + (xy[i][1] - xy[j][1]) ** 2) ** 0.5


for i in range(1 << n):
    # いま都市jにいる
    for j in range(n):
        if dp[i][j] == INF:
            continue
        # 次、都市kに向かう
        for k in range(n):
            # 既に通った都市はスキップ
            if i >> k & 1:
                continue

            v = i | 1 << k
            dp[v][k] = min(dp[v][k], dp[i][j] + euclid_dist(j, k))
print(dp[(1 << n) - 1][0])
