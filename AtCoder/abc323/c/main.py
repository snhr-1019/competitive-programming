n, m = map(int, input().split())
a = list(map(int, input().split()))
a2 = []
for i in range(m):
    a2.append((a[i], i))
a2.sort(reverse=True)

mx = 0
s = []
scores = []
for i in range(n):
    si = input()
    s.append(si)
    score = i + 1
    for j in range(m):
        if si[j] == 'o':
            score += a[j]
    scores.append(score)

mx = max(scores)
for i in range(n):
    ans = 0
    score = scores[i]
    for j in range(m):
        if score >= mx:
            break
        if s[i][a2[j][1]] == 'o':
            continue
        score += a2[j][0]
        ans += 1
    print(ans)
