n = int(input())
a = list(map(int, input().split()))

money = 1000
stock = 0
for i in range(n):
    # 売る
    money += stock * a[i]
    stock = 0

    # 買う
    if i != n - 1 and a[i] < a[i + 1]:
        stock = money // a[i]
        money %= a[i]

print(money)
