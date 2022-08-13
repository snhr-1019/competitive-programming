h1, w1 = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h1)]

h2, w2 = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(h2)]

for i in range(2 ** h1):
    for j in range(2 ** w1):
        a_after = []
        for r in range(h1):
            if (i >> r) & 1:
                tmp = []
                for c in range(w1):
                    if (j >> c) & 1:
                        tmp.append(a[r][c])
                a_after.append(tmp)
        # print("--------------")
        # print(a_after)
        if b == a_after:
            print("Yes")
            exit()
print("No")
