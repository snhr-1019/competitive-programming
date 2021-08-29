from collections import deque

N, M = map(int, input().split())

a = list()
current = [[] for _ in range(N + 1)]
stack = []

for i in range(M):
    k = int(input())
    a.append(deque(list(map(int, input().split()))))
    color = a[i].popleft()
    current[color].append(i)
    if len(current[color]) == 2:
        stack.append(color)

done_cnt = 0
while len(stack) != 0:
    color = stack.pop()
    x, y = current[color]
    done_cnt += 1
    if len(a[x]) != 0:
        new_color = a[x].popleft()
        current[new_color].append(x)
        if len(current[new_color]) == 2:
            stack.append(new_color)
    if len(a[y]) != 0:
        new_color = a[y].popleft()
        current[new_color].append(y)
        if len(current[new_color]) == 2:
            stack.append(new_color)

if done_cnt == N:
    print("Yes")
else:
    print("No")
