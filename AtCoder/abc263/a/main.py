A = list(map(int, input().split()))
s = list(set(A))

ca = 0
cb = 0
for a in A:
    if a == s[0]:
        ca += 1
    else:
        cb += 1

if len(s) == 2 and ((ca == 3 and cb == 2) or (ca == 2 and cb == 3)):
    print("Yes")
else:
    print("No")
