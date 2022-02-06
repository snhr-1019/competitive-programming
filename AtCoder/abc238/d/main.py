t = int(input())


def solve():
    a, s = map(int, input().split())

    s -= 2 * a
    if s < 0:
        print("No")
        return
    if a & s == 0:
        print("Yes")
    else:
        print("No")
    return


for i in range(t):
    solve()
