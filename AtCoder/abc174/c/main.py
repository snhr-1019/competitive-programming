k = int(input())

num = 7
cnt = 1
for i in range(k):
    if num % k == 0:
        break

    cnt += 1
    num = (num * 10 + 7) % k

if num % k == 0:
    print(cnt)
else:
    print(-1)

