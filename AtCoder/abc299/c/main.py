n = int(input())
s = input()
if s == '-' * n or s == 'o' * n:
    print(-1)
    exit()

l = s.split('-')

ans = 0
for li in l:
    ans = max(ans, len(li))
print(ans)
