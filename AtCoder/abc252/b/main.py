n, k = map(int, input().split())
a = list(map(int, input().split()))
b = set(map(int, input().split()))

max_a = max(a)

for i in range(n):
    if a[i] == max_a:
        if i + 1 in b:
            print("Yes")
            exit()
print("No")
