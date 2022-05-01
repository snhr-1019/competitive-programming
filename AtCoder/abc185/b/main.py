n, m, t = map(int, input().split())
A = []
B = []
cur_t = 0
cur_n = n
for i in range(m):
    a, b = map(int, input().split())
    cur_n -= a - cur_t
    if cur_n <= 0:
        print("No")
        exit()
    cur_n += b - a
    cur_n = min(cur_n, n)
    cur_t = b

cur_n -= t - cur_t
if cur_n <= 0:
    print("No")
else:
    print("Yes")
