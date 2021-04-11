import math

N, M = map(int, input().split())
A = [0, N + 1]
A.extend([int(x) for x in input().split()])
A.sort()

diff = []
for i in range(1, M + 2):
    d = A[i] - A[i - 1] - 1
    if d > 0:
        diff.append(d)

if len(diff) == 0:
    print(0)
    exit(0)

min_val = min(diff)
ans = 0
for i in diff:
    ans += int(math.ceil(i / min_val))

print(ans)