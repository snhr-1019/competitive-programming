n = int(input())
ans = 1
for i in range(n):
    ans *= sum(list(map(int, input().split())))
    ans %= 10 ** 9 + 7
print(ans)
