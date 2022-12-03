import math


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


######
def solve(k):
    f = factorization(k)
    ans = 0
    for v in f:
        cnt = v[1]
        for t in range(1, v[1] + 1):
            s = v[0] * t
            while s % v[0] == 0:
                s //= v[0]
                cnt -= 1
            if cnt <= 0:
                ans = max(ans, v[0] * t)
                break
    return ans


k = int(input())
print(solve(k))

# for i in range(2, 1000):
#     ans = solve(i)
#     ans2 = 0
#     for j in range(1, i + 1):
#         tmp = math.factorial(j)
#         if tmp % i == 0:
#             ans2 = j
#             break
#     if ans != ans2:
#         print(ans, ans2)
#         print(i)
