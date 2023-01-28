n = int(input())
f = 0
a = 0
for i in range(n):
    s = input()
    if s == "For":
        f += 1
    else:
        a += 1

if f > (f + a) / 2:
    print("Yes")
else:
    print("No")
