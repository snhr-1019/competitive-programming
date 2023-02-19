n, k = map(int, input().split())
s = input()
ans = []
for i in range(n):
    if s[i] == "o" and k > 0:
        ans.append("o")
        k -= 1
    else:
        ans.append("x")
print(*ans, sep="")
