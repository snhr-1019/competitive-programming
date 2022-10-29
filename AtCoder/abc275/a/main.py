n = int(input())
H = list(map(int, input().split()))
m = max(H)

for i in range(n):
    if H[i] == m:
        print(i + 1)
