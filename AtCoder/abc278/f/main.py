n = int(input())
s = [input() for _ in range(n)]

memo = {}


def judge(prev, used):
    if (prev, used) in memo:
        return memo[(prev, used)]
    ret = False
    for i in range(n):
        if (used >> i) & 1:
            continue
        if prev == -1 or s[prev][-1] == s[i][0]:
            ret |= not judge(i, used | 1 << i)
    memo[(prev, used)] = ret
    return ret


if judge(-1, 0):
    print("First")
else:
    print("Second")
