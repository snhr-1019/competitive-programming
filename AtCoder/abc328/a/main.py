n, x = map(int, input().split())
s = list(map(int, input().split()))

print(sum(filter(lambda t: t <= x, s)))
