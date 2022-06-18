n = int(input())
S = []
for _ in range(n):
    l, r = map(int, input().split())
    S.append([l, -1])
    S.append([r, 1])
S.sort()

cur = 0
start = 0
for s in S:
    if cur == 0 and s[1] < 0:
        start = s[0]
    cur -= s[1]
    if cur == 0:
        print(start, s[0])
