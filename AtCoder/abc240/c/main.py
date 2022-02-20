n, x = map(int, input().split())

candidates = set()
candidates.add(0)

for i in range(n):
    a, b = map(int, input().split())
    nxt_cand = set()
    for c in candidates:
        nxt_cand.add(c + a)
        nxt_cand.add(c + b)
    candidates = nxt_cand
if x in candidates:
    print("Yes")
else:
    print("No")

