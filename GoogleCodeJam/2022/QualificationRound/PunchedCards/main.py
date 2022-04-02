def printRow(i, c):
    out1 = []
    for j in range(c):
        out1.append("+")
        out1.append("-")
    out1.append("+")

    out2 = []
    for j in range(c):
        out2.append("|")
        out2.append(".")
    out2.append("|")

    if i == 0:
        out1[0] = "."
        out1[1] = "."
        out2[0] = "."

    print(*out1, sep="")
    print(*out2, sep="")
    if i == r - 1:
        print(*out1, sep="")


def draw(r, c):
    for i in range(r):
        printRow(i, c)


t = int(input())
for i in range(t):
    r, c = map(int, input().split())
    print(f'Case #{i+1}:')
    draw(r, c)