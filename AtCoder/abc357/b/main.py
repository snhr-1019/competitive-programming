s = input()
n = len(s)

l = 0
u = 0
for c in s:
    if c.islower():
        l += 1
    else:
        u += 1
if u > l:
    print(s.upper())
else:
    print(s.lower())

