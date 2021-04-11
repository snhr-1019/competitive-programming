n = int(input())
c = input()

r_cnt = 0
for i in range(n):
    if c[i] == 'R':
        r_cnt += 1


r_cnt_2 = 0
for i in range(r_cnt):
    if c[i] == 'R':
        r_cnt_2 += 1

if r_cnt == n:
    print(0)
else:
    print(r_cnt - r_cnt_2)
