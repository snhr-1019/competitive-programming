N = int(input())

p = [list(map(int, input().split())) for i in range(N)]
p.sort(reverse=True, key=lambda x: (x[0] * 2 + x[1]))

sum_a = 0
for i in range(N):
    sum_a += p[i][0]

sum_b = 0
for i in range(N):
    sum_a -= p[i][0]
    sum_b += p[i][0] + p[i][1]
    if sum_b > sum_a:
        print(i + 1)
        exit(0)
