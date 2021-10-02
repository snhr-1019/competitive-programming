N = int(input())
A = list(input().split())
A_rank = {a: i for i, a in enumerate(sorted(A))}

# 圧縮
A = [A_rank[a] for a in A]
max_A = max(A)
index_dict = [list() for _ in range(max_A + 1)]

for i in range(N):
    index_dict[A[i]].append(i)

ans = 0
for l_index in range(N):
    l_val = A[l_index]
    # rの値で取りうるもの
    for r_val in range(l_val, max_A + 1):
        for r_index in index_dict[r_val]:
            if r_index != l_index:
                ans += 2 ** (r_index - l_index - 1)
                ans %= 99824435
print(ans)
