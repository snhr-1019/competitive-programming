import bisect

N = int(input())
A = [- 10 ** 10] + sorted(list(map(int, input().split()))) + [10 ** 10]
Q = int(input())
ans = []
for i in range(Q):
    B = int(input())
    r = bisect.bisect_right(A, B)
    print(min(B - A[r - 1], A[r] - B))
