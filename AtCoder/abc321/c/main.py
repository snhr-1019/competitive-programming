k = int(input())
cand = []
for i in range(2 ** 10):
    s = []
    for j in range(10):
        if i >> j & 1:
            s.append(j)
    if len(s) == 0:
        continue
    if len(s) == 1 and s == 0:
        continue
    s.reverse()
    cand.append(int(''.join(map(str, s))))
cand.sort()
print(cand[k])
