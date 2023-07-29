from bisect import bisect_left, bisect_right

n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(lambda x: -1 * int(x), input().split())))
# print(a)
# print(b)

l = -1
r = 10 ** 10
while r - l > 1:
    mid = (l + r) // 2
    seller_cnt = bisect_right(a, mid)
    buyer_cnt = bisect_right(b, -1 * mid)
    if seller_cnt >= buyer_cnt:
        r = mid
    else:
        l = mid
print(r)
