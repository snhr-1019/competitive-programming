n, k = map(int, input().split())


def cast(c):
    return ord(c) - ord('a')


cnt = [[0] * 26 for _ in range(n)]
for i in range(n):
    s = input()
    for j in range(len(s)):
        cnt[i][cast(s[j])] += 1

ans = 0
for i in range(2 ** n):
    cnt_sum = [0] * 26
    for j in range(n):
        if (i >> j) & 1:
            for m in range(26):
                cnt_sum[m] += cnt[j][m]
    ans = max(ans, len(list(filter(lambda x: x == k, cnt_sum))))
print(ans)
