s = input()
n = int(input())
l = len(s)

mx = 0
mn = 0
for i in range(l):
    mx *= 2
    mn *= 2
    if s[i] == "?":
        mx += 1
    else:
        mn += int(s[i])

if n < mn:
    print(-1)
    exit()

ans = mn
for i in range(l):
    if s[i] == "?":
        if n - ans >= 2 ** (l - i - 1):
            ans += 2 ** (l - i - 1)
print(ans)
