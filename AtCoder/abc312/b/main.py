n, m = map(int, input().split())
s = [list(input()) for _ in range(n)]


def is_tak(i, j):
    for a in range(i, i + 4):
        for b in range(j, j + 4):
            if a == i + 3 or b == j + 3:
                if s[a][b] != '.':
                    return False
            else:
                if s[a][b] != '#':
                    return False

    for a in range(i + 5, i + 9):
        for b in range(j + 5, j + 9):
            if a == i + 5 or b == j + 5:
                if s[a][b] != '.':
                    return False
            else:
                if s[a][b] != '#':
                    return False

    return True


for i in range(n - 8):
    for j in range(m - 8):
        if is_tak(i, j):
            print(i + 1, j + 1)
