n = int(input())


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


ans = 0
for i in range(1, n + 1):
    fact = factorization(i)
    need = 1
    for j in range(len(fact)):
        # 平方になっておらず、余る部分
        if fact[j][1] % 2 == 1:
            need *= fact[j][0]
    k = 1
    while need * (k + 1) * (k + 1) <= n:
        k += 1
    ans += k
print(ans)
