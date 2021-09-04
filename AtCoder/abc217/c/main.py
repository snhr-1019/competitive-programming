n = int(input())
p = [0] + list(map(int, input().split()))
q = [0] * (n + 1)

for i in range(1, n + 1):
    q[p[i]] = i

print(" ".join(map(str, q[1:])))
