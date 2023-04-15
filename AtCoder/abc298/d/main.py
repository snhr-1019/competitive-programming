from collections import deque

M = 998244353
q = int(input())

que = deque()
que.append("1")
val = 1
for _ in range(q):
    query = input().split()
    if query[0] == '1':
        que.append(query[1])
        val = ((val * 10) % M + int(query[1])) % M
    elif query[0] == '2':
        s = que.popleft()
        val = (val - int(s) * pow(10, len(que), M)) % M
    elif query[0] == '3':
        print(val)
