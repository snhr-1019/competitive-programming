n, t = map(int, input().split())
a = list(map(int, input().split()))

rows = [set()] * n

for i in range(n):
    s = set()
    for j in range(n):
        s.add((i * n) + (j + 1))
    rows[i] = s

columns = [set()] * n
for i in range(n):
    s = set()
    for j in range(n):
        s.add((j * n) + (i + 1))
    columns[i] = s

diagonals = [set()] * 2

x = set()
y = set()
for i in range(n):
    x.add((i * n) + (i + 1))
    y.add((i * n) + (n - i))
diagonals[0] = x
diagonals[1] = y

for i in range(t):
    x = (a[i] - 1) % n
    y = (a[i] - 1) // n

    rows[y].remove(a[i])
    if len(rows[y]) == 0:
        print(i + 1)
        exit()

    columns[x].remove(a[i])
    if len(columns[x]) == 0:
        print(i + 1)
        exit()

    if x == y:
        diagonals[0].remove(a[i])
        if len(diagonals[0]) == 0:
            print(i + 1)
            exit()
    if x + y == n - 1:
        diagonals[1].remove(a[i])
        if len(diagonals[1]) == 0:
            print(i + 1)
            exit()
print(-1)
