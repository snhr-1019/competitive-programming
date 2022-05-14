n = int(input())

ans = []
for i in range(3):
    for k in range(1, 10 ** 2 + 1):
        ans.append(k * (10 ** 2) ** i)
print(len(ans))
print(*ans)
