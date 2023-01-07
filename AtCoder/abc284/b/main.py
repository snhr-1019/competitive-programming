t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for a in A:
        if a % 2 == 1:
            ans += 1
    print(ans)
