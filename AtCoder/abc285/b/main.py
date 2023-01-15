n = int(input())
s = input()
t = len(s)


def solve(i):
    a = s[:t - i]
    b = s[i:]
    for l in range(t - i):
        if a[l] == b[l]:
            print(l)
            return
    print(t - i)


for i in range(1, n):
    solve(i)
