h, w = map(int, input().split())
S = [[] for _ in range(w)]
for i in range(h):
    s = input()
    for j in range(w):
        S[j].append(s[j])
T = [[] for _ in range(w)]
for i in range(h):
    t = input()
    for j in range(w):
        T[j].append(t[j])

S.sort()
T.sort()

if S == T:
    print("Yes")
else:
    print("No")
