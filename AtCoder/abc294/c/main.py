n, m = map(int, input().split())
a = list(map(int, input().split())) + [10 ** 10]
b = list(map(int, input().split())) + [10 ** 10]
ans_a = [0] * n
ans_b = [0] * m

ai = 0
bi = 0

for i in range(1, n + m + 1):
    if a[ai] < b[bi]:
        ans_a[ai] = i
        ai += 1
    else:
        ans_b[bi] = i
        bi += 1

print(*ans_a)
print(*ans_b)
