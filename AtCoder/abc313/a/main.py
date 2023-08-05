n = int(input())
p = list(map(int, input().split()))

ans = 0
while True:
    if p.count(p[0]) == 1 and p[0] == max(p):
        print(ans)
        exit()
    ans += 1
    p[0] += 1