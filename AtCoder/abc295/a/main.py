n = input()
w = list(input().split())


def is_ok(w):
    return w in ("and", "not", "that", "the", "you")


for wi in w:
    if is_ok(wi):
        print("Yes")
        exit()
print("No")
