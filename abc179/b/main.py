N = int(input())

max_cnt = 0
cnt = 0
for i in range(N):
    a, b = map(int, input().split())
    if a == b:
        cnt += 1
    else:
        cnt = 0
    max_cnt = max(max_cnt, cnt)

if max_cnt >= 3:
    print("Yes")
else:
    print("No")
