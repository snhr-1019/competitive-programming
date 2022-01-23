s = list(input())
a, b = map(int, input().split())
a -= 1
b -= 1
tmp = s[a]
s[a] = s[b]
s[b] = tmp
print("".join(s))
