from collections import Counter

hint = {i: s for i, s in enumerate(list(input()))}

ans = 0
for i in range(10000):
    c = Counter(list(str(i).zfill(4)))
    ok = True
    for n in range(10):
        if hint[n] == 'o' and c[str(n)] == 0:
            ok = False
            break
        elif hint[n] == 'x' and c[str(n)] > 0:
            ok = False
            break
    if ok:
        ans += 1
print(ans)
