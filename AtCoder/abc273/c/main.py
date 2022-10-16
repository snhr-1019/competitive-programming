from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))
B = sorted(list(set(A)), reverse=True)

cnt = dict()
for i in range(len(B)):
    cnt[B[i]] = i

ans = [0] * n
for a in A:
    ans[cnt[a]] += 1
print(*ans, sep="\n")
