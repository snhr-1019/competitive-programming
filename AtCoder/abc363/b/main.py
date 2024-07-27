n, t, p = map(int, input().split())
l = list(map(int, input().split()))

for i in range(t):
    cnt = 0
    for j in range(n):
        cnt += l[j] + i >= t

    if cnt >= p:
        print(i)
        exit()
