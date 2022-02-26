import bisect

q = int(input())
a = []
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        a.append(query[1])
    else:
        a.sort()
        x = query[1]
        k = query[2]
        if query[0] == 2:
            t = bisect.bisect_right(a, x)
            # print(t)
            if t - k >= 0:
                print(a[t - k])
            else:
                print(-1)
        elif query[0] == 3:
            t = bisect.bisect_left(a, x) - 1
            if t + k < len(a):
                print(a[t + k])
            else:
                print(-1)
