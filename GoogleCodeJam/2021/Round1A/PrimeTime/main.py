T = int(input())

for case in range(T):
    M = int(input())
    cards = []
    n = 0
    for i in range(M):
        j, k = map(int, input().split())
        cards += [j] * k
        n += k

    ans = 0
    for i in range(2 ** n):
        sm = 0
        product = 1
        for j in range(n):
            if (i >> j) & 1:
                product *= cards[j]
            else:
                sm += cards[j]
        if product == sm:
            ans = max(ans, sm)
    print("Case #%d: %d" % (case + 1, ans))
