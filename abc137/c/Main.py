n = int(input())
s = [input() for i in range(n)]
sdict = {}

for i in range(n):
    sortedstr = ''.join(sorted(s[i]))
    if sortedstr in sdict:
        sdict[sortedstr] = sdict[sortedstr] + 1
    else:
        sdict[sortedstr] = 1

ans = 0
for key in sdict.keys():
    cnt = sdict[key]
    ans += int(cnt * (cnt-1) / 2)
print(ans)
