n, m = map(int, input().split())
s = [input() for _ in range(n)]
ans = 0


def is_ok(i, j):
    for k in range(m):
        if s[i][k] == 'x' and s[j][k] == 'x':
            return False
    return True


for i in range(n - 1):
    for j in range(i + 1, n):
        if is_ok(i, j):
            ans += 1
print(ans)
