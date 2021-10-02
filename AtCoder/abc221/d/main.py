from collections import defaultdict

N = int(input())
diff = defaultdict(int)
day_count = [0] * (N + 1)
for i in range(N):
    a, b = map(int, input().split())
    # a日目に1人増え、a+b日目に1人減る
    diff[a] += 1
    diff[a + b] -= 1

num = 0
cnt = 0
sorted_diff = sorted(diff.items())
before_day = 0
for d in sorted_diff:
    day = d[0]
    day_count[cnt] += day - before_day
    before_day = day
    cnt += d[1]

print(*day_count[1:])
