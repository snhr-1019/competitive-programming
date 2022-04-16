from bisect import bisect_left

n = int(input())
a = list(map(int, input().split()))

appearance = [[] for _ in range(n + 1)]
cnt = [0] * (n + 1)
for i in range(n):
    appearance[a[i]].append(i)
    cnt[a[i]] += 1

q = int(input())

for i in range(q):
    l, r, x = map(int, input().split())
    a_list = appearance[x]
    l -= 1
    r -= 1
    l_cnt = bisect_left(a_list, l)
    r_cnt = bisect_left(a_list, r + 1)
    print(r_cnt - l_cnt)
