N, K = map(int, input().split())

a = [0] * N
b = [0] * N
q = []
ans = 0
for i in range(N):
    a, b = map(int, input().split())
    q.append(b)
    q.append(a - b)
print(sum(sorted(q, reverse=True)[0:K]))
