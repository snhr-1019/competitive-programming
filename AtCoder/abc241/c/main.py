n = int(input())
s = []
for i in range(n):
    s.append(list(input()))

# 横方向でできるか
ans = False
for i in range(n):
    cnt = 0
    dot_cnt = 0
    for j in range(n):
        cnt += 1

        if s[i][j] == '.':
            dot_cnt += 1

        if cnt > 6:
            if s[i][j - 7] == '.':
                dot_cnt -= 1
            cnt -= 1

        if cnt == 6 and dot_cnt <= 2:
            ans = True

# 縦方向でできるか
for j in range(n):
    cnt = 0
    dot_cnt = 0
    for i in range(n):
        cnt += 1

        if s[i][j] == '.':
            dot_cnt += 1

        if cnt > 6:
            if s[i - 7][j] == '.':
                dot_cnt -= 1
            cnt -= 1

        if cnt == 6 and dot_cnt <= 2:
            ans = True

if ans:
    print("Yes")
else:
    print("No")
