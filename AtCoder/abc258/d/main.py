n, x = map(int, input().split())

# iステージ目までの初回クリアの合計時間
sm = [0] * n
# iステージ目までのうちのプレイ時間のみの最小時間
mn = [0] * n
cur_sm = 0
cur_mn = 10 ** 10
for i in range(n):
    a, b = map(int, input().split())
    cur_sm += a + b
    sm[i] = cur_sm

    cur_mn = min(cur_mn, b)
    mn[i] = cur_mn

ans = 10 ** 20
for i in range(n):
    time = sm[i] + mn[i] * (x - i - 1)
    ans = min(ans, time)
print(ans)
