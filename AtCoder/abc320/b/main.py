s = input()
n = len(s)
ans = 0


def is_ok(s):
    return s == s[::-1]


for i in range(n):
    for j in range(i, n):
        if is_ok(s[i:j + 1]):
            ans = max(ans, j - i + 1)
print(ans)
