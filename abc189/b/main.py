N, X = map(int, input().split())

alcohol = 0
for i in range(N):
    V, P = map(int, input().split())
    alcohol += V * P / 100
    if alcohol > X:
        print(i + 1)
        exit(0)
print(-1)
