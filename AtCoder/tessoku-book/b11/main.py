from bisect import bisect_left

n = int(input())
a = sorted(list(map(int, input().split())))
q = int(input())
for _ in range(q):
    x = int(input())
    print(bisect_left(a, x))
