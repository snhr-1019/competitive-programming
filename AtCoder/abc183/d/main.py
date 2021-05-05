N, W = map(int, input().split())
S = tuple(tuple(map(int, input().split())) for i in range(N))

arr = [0 for i in range(2 * 10 ** 5 + 1)]

for s in S:
    arr[s[0]] += s[2]
    arr[s[1]] -= s[2]

w = 0
for c in arr:
    w += c
    if w > W:
        print("No")
        exit()
print("Yes")
