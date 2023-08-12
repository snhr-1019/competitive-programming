n, m = map(int, input().split())
s = list(input())
c = list(map(lambda x: int(x) - 1, input().split()))

cc = [[] for _ in range(m)]

for i in range(n):
    cc[c[i]].append(i)

for i in range(m):
    t = s[cc[i][-1]]
    for j in range(len(cc[i])):
        tmp = s[cc[i][j]]
        s[cc[i][j]] = t
        t = tmp
print(*s, sep='')
