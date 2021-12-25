X = input()
lst = list(map(int, list(X)))
s = [0] * len(lst)
s[0] = lst[0]
for i in range(1, len(lst)):
    s[i] = s[i - 1] + lst[i]
s.reverse()

ans_l = []
up = 0
for i in range(len(lst)):
    ans_l.append((s[i] + up) % 10)
    up = (s[i] + up) // 10
if up != 0:
    ans_l.append(up)
ans_l.reverse()
print(''.join(map(str, ans_l)))
