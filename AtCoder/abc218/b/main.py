p = list(map(int, input().split()))

ans = ''
for c in p:
    ans += chr(c + 96)
print(ans)
