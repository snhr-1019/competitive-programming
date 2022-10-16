from collections import defaultdict

q = int(input())
cur = 0
val = [-1]
parent = [0]
notebook = defaultdict(int)
for _ in range(q):
    query = list(input().split())
    command = query[0]
    if command == 'ADD':
        x = int(query[1])
        val.append(x)
        parent.append(cur)
        cur = len(parent) - 1
    elif command == 'DELETE':
        cur = parent[cur]
    elif command == 'SAVE':
        y = int(query[1])
        notebook[y] = cur
    elif command == 'LOAD':
        z = int(query[1])
        cur = notebook[z]
    print(val[cur])
