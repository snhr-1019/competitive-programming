h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]
b = [list(input()) for _ in range(h)]


def vshift():
    global a
    a = a[1:] + [a[0]]


def hshift():
    global b
    for i in range(h):
        b[i] = b[i][1:] + [b[i][0]]


for i in range(h):
    vshift()
    for j in range(w):
        hshift()
        if a == b:
            print("Yes")
            exit()
print("No")
