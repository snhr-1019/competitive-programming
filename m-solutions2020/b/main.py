card = list(map(int, input().split()))
k = int(input())

for i in range(k):
    if card[0] >= card[1]:
        card[1] *= 2
    elif card[1] >= card[2]:
        card[2] *= 2
    else:
        card[2] *= 2

print("Yes") if card[0] < card[1] < card[2] else print("No")
