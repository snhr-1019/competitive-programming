n = int(input())
S = input()

ans = ""
start = False
for s in S:
    if s == '"':
        start = not start
        ans += '"'
    elif s == ',':
        if start:
            ans += ','
        else:
            ans += '.'
    else:
        ans += s
print(ans)
