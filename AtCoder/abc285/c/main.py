s = input()
l = len(s)
ans = 0
for i in range(l):
    ans += (ord(s[-1 - i]) - ord('A') + 1) * 26 ** i
print(ans)
