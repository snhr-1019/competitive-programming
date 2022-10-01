n, s = map(int, input().split())
A = [0] * (n + 1)
B = [0] * (n + 1)
dp = [[-1] * (s + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(1, n + 1):
    a, b = map(int, input().split())
    A[i] = a
    B[i] = b

# 配るDP
for i in range(n):
    for j in range(s):
        if dp[i][j] == -1:
            continue

        # i+1番目のカードを表に置くとき
        if j + A[i + 1] <= s:
            dp[i + 1][j + A[i + 1]] = (dp[i][j] << 1) | 1
        # i+1番目のカードを裏に置くとき
        if j + B[i + 1] <= s:
            dp[i + 1][j + B[i + 1]] = (dp[i][j] << 1) | 0
if dp[n][s] == -1:
    print("No")
    exit()
else:
    print("Yes")
ans = []
for i in range(n):
    if (dp[n][s] >> i) & 1:
        ans.append("H")
    else:
        ans.append("T")
print(*reversed(ans), sep="")
