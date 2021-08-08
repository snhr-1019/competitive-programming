import heapq

Q = int(input())

a = []
heapq.heapify(a)
b = 0
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        heapq.heappush(a, query[1] - b)
    elif query[0] == 2:
        b += query[1]
    elif query[0] == 3:
        print(heapq.heappop(a) + b)
