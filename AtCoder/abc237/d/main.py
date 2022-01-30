n = int(input())
s = "a" + input()
link = [[-1, -1] for _ in range(n + 1)]
first = 0

for i in range(1, n + 1):
    prev = link[i - 1][0]
    nxt = link[i - 1][1]
    if s[i] == 'L':
        link[prev][1] = i
        link[i][0] = prev
        link[i][1] = i - 1
        link[i - 1][0] = i
        if i - 1 == first:
            first = i
    else:
        link[nxt][0] = i
        link[i][0] = i - 1
        link[i][1] = nxt
        link[i - 1][1] = i

#print(first)
#print(link)

ans = [first]
nxt = first
while True:
    nxt = link[nxt][1]
    if nxt == -1:
        break
    ans.append(nxt)
print(*ans)
