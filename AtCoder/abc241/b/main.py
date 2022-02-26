n, m = map(int, input().split())
a = list(map(int, input().split()))

a_cnt = {v: 0 for v in list(set(a))}

for i in range(n):
    a_cnt[a[i]] += 1

b = list(map(int, input().split()))

for i in range(m):
    if b[i] not in a_cnt or a_cnt[b[i]] <= 0:
        print("No")
        exit()
    a_cnt[b[i]] -= 1
print("Yes")
