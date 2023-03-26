from bisect import bisect

n, x = map(int, input().split())
a = list(map(int, input().split()))
print(bisect(a, x))
