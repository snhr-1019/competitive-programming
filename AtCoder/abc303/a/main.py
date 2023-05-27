n = int(input())
s = input()
t = input()


def similar(a, b):
    return a == b or {a, b} == {'1', 'l'} or {a, b} == {'0', 'o'}


if all(similar(s[i], t[i]) for i in range(n)):
    print("Yes")
else:
    print("No")
