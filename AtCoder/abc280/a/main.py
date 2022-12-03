h, w = map(int, input().split())
ans = 0
for i in range(h):
    S = input()
    for s in S:
        if s == '#':
            ans += 1
print(ans)
