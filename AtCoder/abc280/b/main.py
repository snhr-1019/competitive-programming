n = int(input())
s = [0] + list(map(int, input().split()))
for i in range(1, n + 1):
    print(s[i] - s[i - 1])
