n, m = map(int, input().split())
a = list(map(lambda x: [int(x), 0], input().split()))
b = list(map(lambda x: [int(x), 1], input().split()))

s = sorted(a + b)

for i in range(n + m - 1):
    if s[i][1] == s[i + 1][1] == 0:
        print("Yes")
        exit()
print("No")
