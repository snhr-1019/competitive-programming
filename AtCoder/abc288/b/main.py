n, k = map(int, input().split())
s = [input() for _ in range(n)]
print(*sorted(s[:k]))
