n = int(input())
s = []
for i in range(n):
    s.append(list(map(int, input())))


def solve(k):
    ret = 0
    for i in range(10):
        cnt = 0
        for j in range(n):
            if s[j][i] == k:
                cnt += 1
        if cnt > 0:
            ret = max(ret, i + 10 * (cnt - 1))
    return ret

ans = 10 ** 9
for i in range(10):
    ans = min(ans, solve(i))
print(ans)
