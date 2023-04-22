import sys

n = int(input())


def is_one(x):
    print("? " + str(x))
    sys.stdout.flush()
    return input() == "1"


l = 1
r = n
while r - l > 1:
    m = (l + r) // 2
    if is_one(m):
        r = m
    else:
        l = m
print("! " + str(l))
