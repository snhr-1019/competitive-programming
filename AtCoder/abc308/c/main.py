n = int(input())

f = []

for i in range(n):
    a, b = map(int, input().split())
    f.append((-1 * (a * 10 ** 20 // (a + b)), i))

f.sort()

ans = []
for fi in f:
    print(fi[1] + 1)
