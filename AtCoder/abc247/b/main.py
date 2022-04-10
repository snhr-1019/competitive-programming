from collections import defaultdict

cnt = defaultdict(int)

n = int(input())
S = []
T = []
for i in range(n):
    s, t = input().split()
    S.append(s)
    T.append(t)
    cnt[s] += 1
    cnt[t] += 1

for i in range(n):
    s_ok = True
    t_ok = True
    for j in range(n):
        if i == j:
            continue
        if S[i] == S[j] or S[i] == T[j]:
            s_ok = False
        if T[i] == S[j] or T[i] == T[j]:
            t_ok = False
        if not s_ok and not t_ok:
            print("No")
            exit()
print("Yes")

