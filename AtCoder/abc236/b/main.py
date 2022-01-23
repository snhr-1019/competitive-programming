n = int(input())
a = list(map(int, input().split()))

cnt = [0] * (n + 1)

for v in a:
    cnt[v] += 1

for i in range(1, n + 1):
    if cnt[i] == 3:
        print(i)
