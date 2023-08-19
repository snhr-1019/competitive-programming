m = int(input())
d = list(map(int, input().split()))

s = (sum(d) + 1) // 2

for i in range(m):
    if s <= d[i]:
        print(i + 1, s)
        break
    s -= d[i]
