S = input()
T = input()

d = set()
for i in range(len(S)):
    s = ord(S[i])
    t = ord(T[i])
    if t - s < 0:
        tmp = 26 + t - s
    else:
        tmp = t - s
    d.add(tmp)
if len(d) == 1:
    print("Yes")
else:
    print("No")
