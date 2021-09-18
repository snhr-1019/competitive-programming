T = list(input())

ans = list()
reverse = False
for c in T:
    if c == 'R':
        reverse = not reverse
        continue

    if not reverse:
        if len(ans) == 0 or ans[-1] != c:
            ans.append(c)
        else:
            ans.remove(-1)
            del ans[-1]
    else:
        if len(ans) == 0 or ans[0] != c:
            ans.insert(0, c)
        else:
            del ans[0]

if not reverse:
    print(''.join(ans))
else:
    print(''.join(reversed(ans)))