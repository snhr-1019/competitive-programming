T = int(input())
for case in range(T):
    N = int(input())
    L = list(map(int, input().split()))

    cost = 0
    for i in range(N - 1):
        j = L.index(min(L[i:N]))
        L = L[0:i] + list(reversed(L[i:j + 1])) + L[j + 1:N]
        cost += j - i + 1
    print("Case #%d: %d" % (case + 1, cost))
