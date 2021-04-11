import itertools

n, d = map(int, input().split())

x = [list(map(int, input().split())) for i in range(n)]

cnt = 0
for c in itertools.combinations(range(n), 2):
    sum = 0
    for i in range(d):
        sum += (x[c[0]][i] - x[c[1]][i])**2
    dist = sum**0.5

    if dist.is_integer():
        cnt += 1

print(cnt)