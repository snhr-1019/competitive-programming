s = input()
n = len(s)
xy = []
z = -1
r = []
for i in range(n):
    if s[i] == "B":
        xy.append(i)
    if s[i] == "K":
        z = i
    if s[i] == "R":
        r.append(i)

if sum(xy) % 2 == 1 and r[0] < z < r[1]:
    print("Yes")
else:
    print("No")
