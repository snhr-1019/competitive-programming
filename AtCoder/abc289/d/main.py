n = int(input())
a = list(map(int, input().split()))
m = int(input())
bb = list(map(int, input().split()))
mochi = [False] * (2 * 10 ** 5)
for t in bb:
    mochi[t] = True

x = int(input())
dp = [False] * (2 * 10 ** 5)
dp[0] = True

for i in range(x + 1):
    if not dp[i]:
        continue

    for aa in a:
        if not mochi[i + aa]:
            dp[i + aa] = True
if dp[x]:
    print("Yes")
else:
    print("No")
