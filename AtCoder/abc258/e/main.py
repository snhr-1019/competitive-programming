n, q, x = map(int, input().split())
w = list(map(int, input().split()))


def nextbox(cur):
    weight = 0
    cnt = 0
    while weight < x:
        weight += w[cur]
        cur = (cur + 1) % n
        cnt += 1
    return cur, cnt


cur_potato = 0

visited = [-1] * n
visited[0] = 0

boxes = []
rest = 0
loop = 0
while True:
    nxt_potato, cnt_potato = nextbox(cur_potato)
    visited[cur_potato] = len(boxes)
    boxes.append(cnt_potato)
    if visited[nxt_potato] != -1:
        rest = visited[nxt_potato]
        loop = len(boxes) - rest
        break

    cur_potato = nxt_potato

for i in range(q):
    k = int(input()) - 1
    if k <= loop:
        print(boxes[k])
    else:
        index = rest + (k - rest) % loop
        print(boxes[index])
