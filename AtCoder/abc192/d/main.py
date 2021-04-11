X = input()
M = int(input())

d = max(list(map(int, X)))


def f(str, d):
    ret = 0
    for i in range(len(str)):
        ret += int(str[i]) * d ** i
    return ret


ans = 0
while True:
    d += 1
    if f(X, d) <= M:
        ans += 1
    else:
        print(ans)
        exit()
