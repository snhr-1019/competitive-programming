n = int(input())
a = list(map(int, input().split()))

approved = True
for i in range(n):
    if a[i] % 2 == 0 and (a[i] % 3 != 0 and a[i] % 5 != 0):
        approved = False
        break
print("APPROVED" if approved else "DENIED")
