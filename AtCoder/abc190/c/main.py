N, M = map(int, input().split())
As = []
Bs = []
for i in range(M):
    A, B = map(int, input().split())
    As.append(A - 1)
    Bs.append(B - 1)
K = int(input())
Cs = []
Ds = []
for i in range(K):
    C, D = map(int, input().split())
    Cs.append(C - 1)
    Ds.append(D - 1)

ans = 0
for i in range(2 ** K):
    dish = [0] * N
    for j in range(K):
        if (i >> j) & 1:
            dish[Ds[j]] += 1
        else:
            dish[Cs[j]] += 1
    cnt = 0
    for k in range(M):
        if dish[As[k]] > 0 and dish[Bs[k]] > 0:
            cnt += 1
    ans = max(ans, cnt)
print(ans)
