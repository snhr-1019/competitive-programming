n = int(input())
a = [0] + list(map(int, input().split()))

ans = 0
same = 0
for i in range(1, n + 1):
    j = a[i]
    if i == j:
        same += 1
        continue
    elif j < i:
        continue
    elif i < j:
        if a[j] == i:
            ans += 1
print(ans + same * (same - 1) // 2)
