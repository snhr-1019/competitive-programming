X = {c: chr(65 + i) for i, c in enumerate(list(input()))}
N = int(input())
l = []
for i in range(N):
    s = input()
    t = ""
    for c in list(s):
        t += X[c]
    l.append((s, t))
l.sort(key=lambda x: x[1])
for v in l:
    print(v[0])
