N = int(input())

ans = list()

while N != 0:
    if N % 2 == 0:
        ans.append("B")
        N //= 2
    else:
        ans.append("A")
        N -= 1
print("".join(reversed(ans)))
