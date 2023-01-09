n = int(input())
a = [0] + list(map(int, input().split()))
win_acc = [0] * (n + 1)
lose_acc = [0] * (n + 1)

for i in range(1, n + 1):
    win_acc[i] = win_acc[i - 1] + a[i]
    lose_acc[i] = lose_acc[i - 1] + (not a[i])

q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    win = win_acc[r] - win_acc[l - 1]
    lose = lose_acc[r] - lose_acc[l - 1]
    if win > lose:
        print("win")
    elif win < lose:
        print("lose")
    else:
        print("draw")

