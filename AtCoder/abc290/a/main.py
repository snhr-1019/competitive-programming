n, m = map(int, input().split())
a = [0] + list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for bb in b:
    ans += a[bb]
print(ans)
