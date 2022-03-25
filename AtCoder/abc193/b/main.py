n = int(input())
A = []
B = []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

cand = []
for i in range(n):
    for j in range(n):
        if i == j:
            cand.append(A[i] + B[j])
        else:
            cand.append(max(A[i], B[j]))
cand.sort()
print(cand[0])
