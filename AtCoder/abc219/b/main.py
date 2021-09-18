S = [input() for _ in range(3)]
T = map(int, list(input()))
ans = ""
for i in T:
    ans += S[i - 1]
print(ans)
