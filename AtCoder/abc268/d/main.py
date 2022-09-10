from itertools import permutations

n, m = map(int, input().split())
S = []
l = 0
T = set()
for i in range(n):
    s = input()
    l += len(s)
    S.append(s)

for _ in range(m):
    T.add(input())


def dfs(name, remain, i):
    name += v[i]

    # 最後だったら適合してるか確認して終わり
    if i == n - 1:
        if 3 <= len(name) <= 16 and name not in T:
            print(name)
            exit()
        return

    # 最後でない場合はアンダースコアを1つ以上追加して次の文字列に進む
    for k in range(1, remain + 1):
        dfs(name + '_' * k, remain - k, i + 1)


# アンダースコアが使える残りの回数
remain = 16 - l

for v in permutations(S):
    dfs("", remain, 0)
print(-1)
