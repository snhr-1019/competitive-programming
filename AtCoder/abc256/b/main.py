n = int(input())
t = []
A = list(map(int, input().split()))
ans = 0
for a in A:
    t.append(0)
    for i in range(len(t)):
        t[i] += a

ans = 0
for s in t:
    if s >= 4:
        ans += 1
print(ans)
