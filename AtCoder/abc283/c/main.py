s = input()
l = len(s)
i = 0
ans = 0
while i < l:
    if i < l - 1 and s[i] == '0' and s[i + 1] == '0':
        ans += 1
        i += 2
    else:
        ans += 1
        i += 1
print(ans)
