t = int(input())


def solve():
    a, s = map(int, input().split())
    a_bin = dec2bin(a)

    for v in a_bin:
        s -= 2 ** v * 2
    if s < 0:
        print("No")
        return

    s_bin = dec2bin(s)
    a_set = set(a_bin)
    s_set = set(s_bin)
    if a_set.isdisjoint(s_set):
        print("Yes")
    else:
        print("No")
    return


def dec2bin(target):
    amari = []
    i = 0
    while target != 0:
        if target % 2 == 1:
            amari.append(i)
        target //= 2
        i += 1
    return amari


for i in range(t):
    solve()
