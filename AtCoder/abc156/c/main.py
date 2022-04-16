n = int(input())
x = list(map(int, input().split()))


def calc(p):
    cost = 0
    for i in range(n):
        cost += (x[i] - p) ** 2
    return cost


ans = 10 ** 9
for p in range(1, 101):
    ans = min(ans, calc(p))

print(ans)
