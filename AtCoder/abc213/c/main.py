H, W, N = map(int, input().split())

h_cards = [1] * H
w_cards = [1] * W

A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    h_cards[a] = 0
    w_cards[b] = 0
    A.append(a)
    B.append(b)

h_sum = [0] * H
h_sum[0] = h_cards[0]
for i in range(1, H):
    h_sum[i] = h_sum[i - 1] + h_cards[i]

w_sum = [0] * W
w_sum[0] = w_cards[0]
for i in range(1, W):
    w_sum[i] = w_sum[i - 1] + w_cards[i]

for i in range(N):
    print(' '.join(map(str, [A[i] - h_sum[A[i]] + 1, B[i] - w_sum[B[i]] + 1])))
