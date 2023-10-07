n = int(input())
cnt = []
for i in range(n):
    cnt.append((-input().count('o'), i))
cnt.sort()
for i in range(n):
    print(cnt[i][1] + 1)
