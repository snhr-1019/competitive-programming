s = input()
t = input()

cur = 0
ans = []
for i in range(len(t)):
    if s[cur] == t[i]:
        cur += 1
        ans.append(i + 1)

print(*ans)
