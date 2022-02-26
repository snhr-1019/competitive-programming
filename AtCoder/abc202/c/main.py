n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(lambda x: int(x) - 1, input().split()))

inv_a = [[] for _ in range(n + 1)]
for i in range(n):
    inv_a[a[i]].append(i)

inv_c = [[] for _ in range(n + 1)]
for i in range(n):
    inv_c[c[i]].append(i)

ans = 0
for i in range(n):
    ans += len(inv_a[b[i]]) * len(inv_c[i])
print(ans)
