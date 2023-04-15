n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]


def rotate(a):
    ret = []
    for x in zip(*a[::-1]):
        ret.append(x)
    return ret


def is_ok(a):
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1 and b[i][j] == 0:
                return False
    return True


for _ in range(4):
    a = rotate(a)
    if is_ok(a):
        print("Yes")
        exit()
print("No")
