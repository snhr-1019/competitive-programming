n = int(input())
changes = dict()
G = [[] for _ in range(n)]
into_num = [0] * n
T = []
for i in range(n):
    s, t = input().split()
    changes[s] = (t, i)
    T.append(t)

for i in range(n):
    t = T[i]
    if t in changes:
        G[i].append(changes[t][1])
        into_num[changes[t][1]] += 1

from collections import deque


def topological_sort(G, into_num):
    # 入ってくる有向辺を持たないノードを列挙
    q = deque()
    # V: 頂点数
    for i in range(n):
        if into_num[i] == 0:
            q.append(i)

    # 以下、幅優先探索
    ans = []
    while q:
        v = q.popleft()
        ans.append(v)
        for adj in G[v]:
            into_num[adj] -= 1  # 入次数を減らす
            if into_num[adj] == 0:
                q.append(adj)  # 入次数が0になったら、キューに入れる

    return ans


ans = topological_sort(G, into_num)  # トポロジカルソート
# トポロジカルソートされたリストの頂点数　と　元のグラフの頂点数を比較
if len(ans) == len(G):
    print('Yes')  # 同じ頂点数なら閉路なし
else:
    print('No')  # 頂点数が異なると閉路が存在している
