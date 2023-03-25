s = input()
l = len(s)
acc = [[0] * (l + 1) for _ in range(10)]

for i in range(l):
    for j in range(10):
        acc[j][i + 1] = acc[j][i] + (s[i] == str(j))


def get_cnt(left, right):
    cnt = [0] * 10
    for i in range(10):
        cnt[i] = acc[i][right] - acc[i][left]
    return cnt


def is_ok(cnt):
    for i in range(10):
        if cnt[i] % 2 == 1:
            return False
    return True


ans = 0
for left in range(l):
    for right in range(left + 2, l + 1, 2):
        cnt = get_cnt(left, right)
        if is_ok(cnt):
            ans += 1
print(ans)
