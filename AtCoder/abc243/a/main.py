v, a, b, c = map(int, input().split())

while True:
    v -= a
    if v < 0:
        print("F")
        exit()
    v -= b
    if v < 0:
        print("M")
        exit()
    v -= c
    if v < 0:
        print("T")
        exit()
