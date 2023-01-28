s = input()
t = input()
len_t = len(t)


# s, tの長さはともにx文字
def match(a, b):
    return a == b or a == '?' or b == '?'


pre = [False] * (len_t + 1)
pre[0] = True
for x in range(len_t):
    if not match(s[x], t[x]):
        break
    pre[x + 1] = True

s = s[::-1]
t = t[::-1]

suf = [False] * (len_t + 1)
suf[0] = True
for x in range(len_t):
    if not match(s[x], t[x]):
        break
    suf[x + 1] = True

for x in range(len_t + 1):
    if pre[x] and suf[len_t - x]:
        print("Yes")
    else:
        print("No")
