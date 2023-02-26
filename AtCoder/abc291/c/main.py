n = int(input())
s = input()

cur = (0, 0)
visited = set()
visited.add(cur)
for c in s:
    if c == 'R':
        nxt = (cur[0] + 1, cur[1])
    elif c == 'L':
        nxt = (cur[0] - 1, cur[1])
    elif c == 'U':
        nxt = (cur[0], cur[1] + 1)
    elif c == 'D':
        nxt = (cur[0], cur[1] - 1)
    if nxt in visited:
        print("Yes")
        exit()
    visited.add(nxt)
    cur = nxt
print("No")
