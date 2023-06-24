n = int(input())
s = [input() for _ in range(n)]


def is_ok(a, b):
    m = a + b
    n = len(m)
    for i in range(n // 2):
        if m[i] != m[~i]:
            return False
    return True


for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if is_ok(s[i], s[j]):
            print("Yes")
            exit()
print("No")
