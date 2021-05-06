from collections import Counter

S = input()
s = Counter(S)
if len(S) <= 2:
    if int(S) % 8 == 0 or int(S[::-1]) % 8 == 0:
        print("Yes")
        exit()
    print("No")
else:
    for i in range(112, 1000, 8):
        c = Counter(str(i))
        ok = True
        for j in c.elements():
            if s[j] < c[j]:
                ok = False
                break
        if ok:
            print("Yes")
            exit()
    print("No")
