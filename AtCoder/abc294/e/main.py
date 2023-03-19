from collections import defaultdict
from sys import stdin

l, n1, n2 = map(int, stdin.readline().split())
v1 = [0] * n1
l1 = [0] * n1
v2 = [0] * n2
l2 = [0] * n2

acc1 = [0] * (n1 + 1)
acc2 = [0] * (n2 + 1)

for i in range(1, n1 + 1):
    v, l = map(int, stdin.readline().split())
    v1[i - 1] = v
    l1[i - 1] = l
    acc1[i] = acc1[i - 1] + l

inv = defaultdict(list)
for i in range(1, n2 + 1):
    v, l = map(int, stdin.readline().split())
    v2[i - 1] = v
    l2[i - 1] = l
    acc2[i] = acc2[i - 1] + l
    inv[v].append(i - 1)

ans = 0
for i in range(n1):
    v = v1[i]
    left1 = acc1[i]
    right1 = acc1[i + 1]

    for j in inv[v]:
        left2 = acc2[j]
        right2 = acc2[j + 1]

        if right1 < left2:
            break

        m_left = max(left1, left2)
        m_right = min(right1, right2)
        if m_left < m_right:
            ans += m_right - m_left
print(ans)
