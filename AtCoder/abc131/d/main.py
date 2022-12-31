n = int(input())
ba = []
for _ in range(n):
    a, b = map(int, input().split())
    ba.append((b, a))
ba.sort()

cur = 0
for v in ba:
    cur += v[1]
    if cur > v[0]:
        print("No")
        exit()
print("Yes")
