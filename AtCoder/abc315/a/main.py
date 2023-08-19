s = input()
ans = []
for si in s:
    if si not in ['a', 'i', 'u', 'e', 'o']:
        ans.append(si)
print(''.join(ans))
