n, t = input().split()
n = int(n)
lt = len(t)

ans = []
for i in range(n):
    s = input()
    ls = len(s)

    if lt == ls:
        # 何もされていない、もしくは1文字変更されている可能性
        cnt = 0
        for j in range(lt):
            if s[j] != t[j]:
                cnt += 1
        if cnt <= 1:
            ans.append(i + 1)

    elif ls + 1 == lt or ls - 1 == lt:
        l = min(ls, lt)

        cnt = 0
        for j in range(l):
            if s[j] == t[j]:
                cnt += 1
            else:
                break
        for j in range(l):
            if s[~j] == t[~j]:
                cnt += 1
            else:
                break
        if cnt >= l:
            ans.append(i + 1)

print(len(ans))
print(*ans)
