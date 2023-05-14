n, m = map(int, input().split())

a = [0]  # 1-indexedに調整
for _ in range(m):
    a.append(int(input().replace(" ", ""), 2))

'''
dp[i][j]
i番目までのクーポンを使用するか否かを決めたときに、
j（買える商品をビットで表したもの）を買うために最小のクーポン枚数
'''
dp = [[1000] * (1 << n) for _ in range(m + 1)]

dp[0][0] = 0

# i番目のクーポンの使用の有無を決める
for i in range(1, m + 1):
    # j: 1つ前のクーポンまでの使用によって買える商品のビット表現
    for j in range(1 << n):
        # i番目のクーポンを使用しない場合
        dp[i][j] = min(dp[i][j], dp[i - 1][j])

        # i番目のクーポンを使用する場合
        v = j | a[i]
        dp[i][v] = min(dp[i][v], dp[i - 1][j] + 1)

if dp[m][(1 << n) - 1] == 1000:
    print(-1)
else:
    print(dp[m][(1 << n) - 1])
