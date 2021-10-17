N = int(input())
A = []
B = []
T = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    T.append(a / b)

left = 0
right = sum(T)
for i in range(N):
    left += T[i]
    right -= T[i]
    # 左の所要時間が大きくなったら、そのときの導火線のどこかでぶつかるはず
    if left >= right:
        left -= T[i]
        right += T[i]

        # ここから2分探索
        l = 0
        r = A[i]
        x = l + r / 2
        left + (x / B[i]) - right + 