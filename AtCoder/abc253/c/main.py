q = int(input())
s = [0] * (2 * 10 ** 5 + 10)

que = []
lst = SortedList(20)

for i in range(q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        x = query[1]

        if s[x] == 0:
            lst.insert(x)
        s[x] += 1

    elif query[0] == 2:
        x = query[1]
        c = query[2]
        s[x] -= min(c, s[x])

        if s[x] == 0:
            lst.remove(x)

    else:
        print(lst[len(lst) - 1] - lst[0])
