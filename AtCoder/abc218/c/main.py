n = int(input())
s = []
t = []
for _ in range(n):
    tmp = input()
    if tmp != '.' * n:
        s.append(list(tmp))
for _ in range(n):
    tmp = input()
    if tmp != '.' * n:
        t.append(list(tmp))

for i in range(len(s[0])):
    tmp_s = []
    ok = True
    for j in range(len(s)):
        if s[j][i] != '.':
            ok = False
    if ok:
        tmp_s.append(s[])
