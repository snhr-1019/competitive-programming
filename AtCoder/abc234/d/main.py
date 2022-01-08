import heapq

n, k = map(int, input().split())
p = list(map(int, input().split()))
q = p[:k]
heapq.heapify(q)
print(q[0])
for i in range(k, n):
    heapq.heappush(q, p[i])
    heapq.heappop(q)
    print(q[0])
