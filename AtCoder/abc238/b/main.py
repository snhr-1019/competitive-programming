n = int(input())
A = map(int, input().split())

cut = [0, 360]
cur = 0
for a in A:
    cur += a
    cur %= 360
    cut.append(cur)
cut.sort()

ans = 0
for i in range(len(cut) - 1):
    ans = max(cut[i + 1] - cut[i], ans)
print(ans)
