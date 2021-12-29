N, L = map(int, input().split())
K = int(input())
A = [0] + list(map(int, input().split())) + [L]


# スコアをs以上にできるかどうか。sより短いものが存在してはいけない
def is_ok(s):
    prev = 0  # 直前の切れ目
    cut = 0
    for i in range(1, N):
        # sを超えたらカット
        if A[i] - A[prev] >= s:
            cut += 1
            prev = i
    return cut >= K and L - A[prev] >= s


ok = -1
ng = L + 1
while ng - ok > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid
print(ok)
