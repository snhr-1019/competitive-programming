n, q = map(int, input().split())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))

for _ in range(q):
    s, t = map(int, input().split())
    s -= 1
    #t -= 1
    print(l[s][t])
