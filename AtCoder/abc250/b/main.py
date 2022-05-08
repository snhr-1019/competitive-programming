n, a, b = map(int, input().split())


def is_black(i, j):
    c = i // a
    r = j // b

    return (r + c) % 2 == 1


for i in range(a * n):
    line = ['.'] * (b * n)
    for j in range(b * n):
        if is_black(i, j):
            line[j] = '#'
    print(''.join(line))
