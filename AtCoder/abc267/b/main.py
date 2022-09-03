s = [0] + list(map(int, list(input())))

if s[1] == 1:
    print("No")
    exit()

c = []
c.append(s[7])
c.append(s[4])
c.append(s[8] or s[2])
c.append(s[5] or s[1])
c.append(s[9] or s[3])
c.append(s[6])
c.append(s[10])

if not c[1] and c[0] and (c[2] or c[3] or c[4] or c[5] or c[6]):
    print("Yes")
    exit()

if not c[2] and (c[0] or c[1]) and (c[3] or c[4] or c[5] or c[6]):
    print("Yes")
    exit()

if not c[3] and (c[0] or c[1] or c[2]) and (c[4] or c[5] or c[6]):
    print("Yes")
    exit()

if not c[4] and (c[0] or c[1] or c[2] or c[3]) and (c[5] or c[6]):
    print("Yes")
    exit()

if not c[5] and (c[0] or c[1] or c[2] or c[3] or c[4]) and c[6]:
    print("Yes")
    exit()

print("No")
