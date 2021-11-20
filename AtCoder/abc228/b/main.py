N, X = map(int, input().split())
A = [0] + list(map(int, input().split()))

known = set()
known.add(X)
cur = X
while A[cur] not in known:
    known.add(A[cur])
    cur = A[cur]
print(len(known))
