k = int(input())
div = set()

i = 1
while i * i <= k:
    if k % i == 0:
        div.add(i)
        div.add(k // i)
    i += 1

div = sorted(list(div))
d = len(div)

ans = 0
for ai in range(d):
    for bi in range(ai, d):
        a = div[ai]
        b = div[bi]
        c = k // a // b
        if a * b * c == k and b <= c:
            ans += 1
print(ans)
