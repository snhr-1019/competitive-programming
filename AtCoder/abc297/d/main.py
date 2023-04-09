a, b = sorted(map(int, input().split()))

ans = 0
while a != b:
    n = -(-(b - a) // a)
    b -= a * n
    ans += n
    a, b = b, a
print(ans)
