n = input()
w = list(input().split())


def is_ok(w):
    return w in {"and", "not", "that", "the", "you"}


if any(is_ok(wi) for wi in w):
    print("Yes")
else:
    print("No")
