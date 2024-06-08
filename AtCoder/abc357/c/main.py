n = int(input())

c = [[""] * 3 ** n for _ in range(3 ** n)]

def f(k, i, j, white=False):
    if white:
        for x in range(3 ** k):
            for y in range(3 ** k):
                c[i + x][j + y] = "."
        return


    if k == 0:
        c[i][j] = "#"
        return


    for x in range(3):
        for y in range(3):
            if x == 1 and y == 1:
                # すべて白
                f(k - 1, i + 3 ** (k - 1), j + 3 ** (k - 1), True)
            else:
                f(k - 1, i + x * 3 ** (k - 1), j + y * 3 ** (k - 1))

f(n, 0, 0)

for i in range(3 ** n):
    print("".join(c[i]))
