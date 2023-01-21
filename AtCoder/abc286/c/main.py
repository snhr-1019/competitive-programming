n, a, b = map(int, input().split())
s = input()

ans = float('inf')
# i: 操作1をする回数
for i in range(n):
    cnt = 0
    # j文字目の一致確認
    for j in range(n // 2):
        if s[(j + i) % n] != s[(n - 1 - j + i) % n]:
            cnt += 1

    ans = min(ans, i * a + cnt * b)

print(ans)
