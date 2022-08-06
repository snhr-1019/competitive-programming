n = int(input())
p = [0, 0] + list(map(int, input().split()))

c = n
ans = 0
while True:
    c = p[c]
    ans += 1
    if c == 1:
        break
print(ans)
