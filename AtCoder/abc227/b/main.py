N = int(input())
S = list(map(int, input().split()))

candidates = set()
for a in range(1, 250):
    for b in range(1, 250):
        candidates.add(4 * a * b + 3 * a + 3 * b)

ans = 0
for s in S:
    if s not in candidates:
        ans += 1
print(ans)
