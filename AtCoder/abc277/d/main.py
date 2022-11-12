n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
s = sum(a)
a *= 2

mx = a[0]
x = a[0]
sum_x = a[0]

for i in range(1, 2 * n+1):
    if a[i] == x or a[i] == (x + 1) % m:
        # i番目のカードが出せる場合
        sum_x += a[i]
        x = a[i]
    else:
        # 出せなければ最大チェック
        mx = max(mx, sum_x)
        sum_x = a[i]
        x = a[i]
print(max(0, s - mx))
