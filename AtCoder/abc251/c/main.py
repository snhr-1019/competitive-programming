n = int(input())
originals = set()
ans = 0
max_score = 0
for i in range(n):
    s, t = input().split()
    t = int(t)
    if s not in originals:
        originals.add(s)
        if t > max_score:
            max_score = t
            ans = i + 1
print(ans)
