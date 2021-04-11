s = input()
t = input()

ans = 100000
for start in range(len(s)-len(t)+1):
    substr = s[start:start+len(t)]

    cnt = len(t)
    for i in range(len(substr)):
        if t[i] == substr[i]:
            cnt -= 1
    ans = min(ans, cnt)

print(ans)
