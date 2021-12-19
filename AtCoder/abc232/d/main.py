import queue

H, W = map(int, input().split())
cnt = [[0] * W for _ in range(H)]

grid = []
for i in range(H):
    grid.append(list(input()) + ["#"])
grid.append(["#"] * (W + 1))

que = queue.Queue()
if grid[0][0] == '.':
    que.put([0, 0])
    cnt[0][0] = 1
else:
    print(0)
    exit()

ans = 1
while not que.empty():
    nxt = que.get()
    h = nxt[0]
    w = nxt[1]
    if grid[h][w + 1] == '.' and cnt[h][w + 1] == 0:
        que.put([h, w + 1])
        cnt[h][w + 1] = cnt[h][w] + 1
        ans = max(ans, cnt[h][w + 1])
    if grid[h + 1][w] == '.' and cnt[h + 1][w] == 0:
        que.put([h + 1, w])
        cnt[h + 1][w] = cnt[h][w] + 1
        ans = max(ans, cnt[h + 1][w])
print(ans)
