from collections import deque

n = int(input())
xyp = []
for i in range(n):
    xyp.append(list(map(int, input().split())))


def is_ok_2(s, start):
    que = deque()
    que.append(start)
    visited = [False] * n
    visited[start] = True
    cnt = 1

    while que:
        cur = que.popleft()
        for nxt in range(n):
            if cur == nxt or visited[nxt]:
                continue
            if xyp[cur][2] * s >= abs(xyp[cur][0] - xyp[nxt][0]) + abs(xyp[cur][1] - xyp[nxt][1]):
                que.append(nxt)
                visited[nxt] = True
                cnt += 1
    return cnt == n


def is_ok(s):
    # 始点を全探索
    for start in range(n):
        # いずれか1つを始点としてすべてに到達できたらそのsはOK
        if is_ok_2(s, start):
            return True
    return False


def binary_search(ok, ng):
    while ok - ng > 1:
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


ok = 10 ** 10
ng = 0

ans = binary_search(ok, ng)
print(ans)
