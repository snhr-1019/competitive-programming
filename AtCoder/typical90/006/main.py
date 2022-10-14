n, k = map(int, input().split())
S = input()

pos = [[-1] * n for _ in range(26)]
for c in range(26):
    cur = -1
    for i in range(n - 1, -1, -1):
        if ord(S[i]) - ord('a') == c:
            cur = i
        pos[c][i] = cur

ans = []
cur = 0
while k > 0:
    for i in range(26):
        if pos[i][cur] != -1 and 0 < k <= n - pos[i][cur]:
            ans.append(chr(i + ord('a')))
            k -= 1
            cur = pos[i][cur] + 1
            break
print(*ans, sep='')
