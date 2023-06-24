ha, wa = map(int, input().split())
a = [list(input()) for _ in range(ha)]

hb, wb = map(int, input().split())
b = [list(input()) for _ in range(hb)]

hx, wx = map(int, input().split())
x = [list(input()) for _ in range(hx)]


def toSet(t):
    s = set()
    for i in range(len(t)):
        for j in range(len(t[0])):
            if t[i][j] == "#":
                s.add((i, j))
    return s


a_set = toSet(a)
b_set = toSet(b)
x_set = toSet(x)

for i in range(-10, 11):
    for j in range(-10, 11):
        for k in range(-10, 11):
            for l in range(-10, 11):
                s = {(ai + i, aj + j) for (ai, aj) in a_set} | {(bi + k, bj + l) for (bi, bj) in b_set}
                if s == x_set:
                    print("Yes")
                    exit()
print("No")
