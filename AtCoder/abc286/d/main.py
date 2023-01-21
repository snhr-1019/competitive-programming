n, x = map(int, input().split())
prices = []
nums = []
for _ in range(n):
    a, b = map(int, input().split())
    prices.append(a)
    nums.append(b)

dp = [False] * (x + 1)
dp[0] = True

# i番目のコインについて考える
for i in range(n):
    ndp = [False] * (x + 1)
    # j円を作れるかを判定
    for j in range(x + 1):
        # i番目のコインをk枚使う
        for k in range(nums[i] + 1):
            if 0 <= j - prices[i] * k <= x:
                ndp[j] |= dp[j - prices[i] * k]
    dp = ndp

if dp[x]:
    print("Yes")
else:
    print("No")
