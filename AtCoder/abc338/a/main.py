s = input()

if s[0].islower():
    print('No')
    exit()

for c in s[1:]:
    if c.isupper():
        print('No')
        exit()
print('Yes')
