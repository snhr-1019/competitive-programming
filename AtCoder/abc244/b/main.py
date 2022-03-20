d = ((1, 0), (0, -1), (-1, 0), (0, 1))

n = int(input())
t = input()
x, y = 0, 0
cur_d = 0
for i in range(n):
    if t[i] == 'S':
        x += d[cur_d][0]
        y += d[cur_d][1]
    else:
        cur_d += 1
        cur_d %= 4
print(x, y)
