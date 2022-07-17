n, x, y, z = map(int, input().split())

p = []
a = list(map(int, input().split()))
b = list(map(int, input().split()))

math = []
english = []
both = []
for i in range(n):
    math.append((-1 * a[i], i + 1))
    english.append((-1 * b[i], i + 1))
    both.append((-1 * (a[i] + b[i]), i + 1))

ok = set()
math.sort()
english.sort()
both.sort()

for i in range(x):
    ok.add(math[i][1])

cnt = 0
for i in range(n):
    if cnt == y:
        break
    if english[i][1] not in ok:
        cnt += 1
        ok.add(english[i][1])

cnt = 0
for i in range(n):
    if cnt == z:
        break
    if both[i][1] not in ok:
        cnt += 1
        ok.add(both[i][1])

print(*sorted(list(ok)), sep="\n")
