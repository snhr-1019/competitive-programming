n, m, k, s, t, x = map(int, input().split())
s -= 1
t -= 1
x -= 1
edges = [[] for _ in range(n)]
MOD = 998244353

for i in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append(v)
    edges[v].append(u)

dp = [[0] * 2 for _ in range(n)]

# dp[a][b] 頂点aにXを通った回数が偶数(b=0)または奇数(b=1)でいられる通りの数
dp[s][0] = 1

# i手目
for i in range(k):
    dp_new = [[0] * 2 for _ in range(n)]
    # 頂点j
    for j in range(n):
        # 偶奇
        for o_e in range(2):
            # if dp[j][o_e] == 0:
            #     continue
            for nxt in edges[j]:
                if nxt == x:
                    dp_new[nxt][not o_e] += dp[j][o_e]
                    dp_new[nxt][not o_e] %= MOD
                else:
                    dp_new[nxt][o_e] += dp[j][o_e]
                    dp_new[nxt][o_e] %= MOD
    dp = dp_new

print(dp[t][0])
