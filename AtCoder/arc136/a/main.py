n = int(input())
s = input()

ans = [s[0]]
for i in range(1, n):
    if ans[-1] == 'B' and s[i] == 'B':
        ans.pop()
        ans.append('A')
    elif ans[-1] == 'B' and s[i] == 'A':
        ans.pop()
        ans.append('A')
        ans.append('B')
    else:
        ans.append(s[i])

print(*ans, sep='')
