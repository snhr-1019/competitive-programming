n = int(input())
a = list(map(int, input().split()))

ave = sum(a) // n


l = 0
h = 0
for ai in a:
    if ai <= ave:
        l += ave - ai
    else:
        h += ai - ave - 1
print(max(l, h))
