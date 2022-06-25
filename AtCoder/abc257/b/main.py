n, k, q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(lambda x: int(x) - 1, input().split()))

for l in L:
    if A[l] == n:
        continue
    if A[l] + 1 not in A:
        A[l] += 1
        continue

print(*A)
