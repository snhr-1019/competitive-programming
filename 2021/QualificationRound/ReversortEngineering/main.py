T = int(input())

for case in range(T):
    N, C = map(int, input().split())

    if C < N - 1 or C > (N + 2) * (N - 1) / 2:
        print("Case #%d: IMPOSSIBLE" % (case + 1))
        continue

    arr = [1] * (N - 1)
    C -= N - 1
    for i in reversed(range(1, N + 1)):
        add = min(C, i - 1)
        arr[i - 2] += add
        C -= add
    arr.reverse()
    ans = [i for i in reversed(range(1, N + 1))]

    for i in range(N - 1):
        ans = ans[0:i] + list(reversed(ans[i:i + arr[i]])) + ans[i + arr[i]:]
    ans.reverse()

    print("Case #%d: %s" % (case + 1, " ".join(map(str, ans))))
