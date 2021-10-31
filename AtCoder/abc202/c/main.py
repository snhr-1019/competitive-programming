N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(lambda x: int(x) - 1, input().split()))

B_m = {}
for i in range(N):
    B_m.setdefault(B[i], [])
    B_m[B[i]].append(i)

C_m = {}
for i in range(N):
    C_m.setdefault(C[i], [])
    C_m[C[i]].append(i)

ans = 0
for a in A:
    if not B_m.get(a):
        continue
    for b in B_m[a]:
        if not C_m.get(b):
            continue
        ans += len(C_m[b])
print(ans)
