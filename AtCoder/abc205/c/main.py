a, b, c = map(int, input().split())

c = (c % 2) + 2

ap = pow(a, c)
bp = pow(b, c)
if ap == bp:
    print("=")
elif ap > bp:
    print(">")
else:
    print("<")
