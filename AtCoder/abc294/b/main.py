h, w = map(int, input().split())

for _ in range(h):
    a = list(map(int, input().split()))
    l = []
    for ai in a:
        if ai == 0:
            l.append('.')
        else:
            l.append(chr(ord('A') + ai - 1))
    print(*l, sep="")
