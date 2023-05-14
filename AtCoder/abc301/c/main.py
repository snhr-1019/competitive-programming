from collections import defaultdict

s = input()
t = input()

cnt_s = defaultdict(int)
cnt_t = defaultdict(int)

for si in s:
    cnt_s[si] += 1
for ti in t:
    cnt_t[ti] += 1

for si in s:
    if si == '@':
        continue

    if cnt_t[si] > 0:
        cnt_t[si] -= 1
    elif si in list('atcoder') and cnt_t['@'] > 0:
        cnt_t['@'] -= 1
    else:
        print("No")
        exit()

for ti in t:
    if ti == '@':
        continue

    if cnt_s[ti] > 0:
        cnt_s[ti] -= 1
    elif ti in list('atcoder') and cnt_s['@'] > 0:
        cnt_s['@'] -= 1
    else:
        print("No")
        exit()
print("Yes")
