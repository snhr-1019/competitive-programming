H, W, N, h, w = map(int, input().split())
A = []
for _ in range(H):
    A.append(list(map(int, input().split())))

all_cnt = [0] * 301

for i in range(H):
    for j in range(W):
        all_cnt[A[i][j]] += 1


def diff_cnt(filled_cnt):
    ans = 0
    for i in range(1, 301):
        if all_cnt[i] - filled_cnt[i] > 0:
            ans += 1
    return ans


# 縦にずれる
for i in range(H - h + 1):
    ans = []
    filled_cnt = [0] * 301
    for t in range(h):
        for s in range(w):
            filled_cnt[A[i + t][s]] += 1
    ans.append(diff_cnt(filled_cnt))

    # 横にずれる
    for j in range(1, W - w + 1):
        # 範囲に入ったところ、外れたところの回数を調整
        for t in range(i, i + h):
            filled_cnt[A[t][j - 1]] -= 1
            filled_cnt[A[t][j + w - 1]] += 1
        ans.append(diff_cnt(filled_cnt))
    print(*ans)
