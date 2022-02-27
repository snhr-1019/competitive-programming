n = int(input())
s = []
for i in range(n):
    s.append(list(input()))

dx = [1, 0, 1, 1]
dy = [0, 1, 1, -1]

for i in range(n):
    for j in range(n):
        for k in range(4):
            dot_cnt = 0
            for l in range(6):
                x = i + dx[k] * l
                y = j + dy[k] * l
                if not (0 <= x < n and 0 <= y < n):
                    dot_cnt = 100
                    break
                if s[i + dx[k] * l][j + dy[k] * l] == '.':
                    dot_cnt += 1

            if dot_cnt <= 2:
                print("Yes")
                exit()
print("No")
