from collections import deque

N = int(input())
T = []
K = []
A = []
for i in range(N):
    tmp = list(map(int, input().split()))
    T.append(tmp[0])
    K.append(tmp[1])
    A.append(list(map(lambda x: x - 1, tmp[2:])))

que = deque()
que.extend(A[N - 1])
ans = T[N - 1]
learned = {N - 1}
while que:
    s = que.pop()
    if s not in learned:
        ans += T[s]
        learned.add(s)
        que.extend(A[s])
print(ans)
