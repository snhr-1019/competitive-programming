N = int(input())
A, B, C = map(int, input().split())
ans = 10 ** 10
for na in range(9999):
    if A * na > N:
        break
    for nb in range(9999):
        if A * na + B * nb > N:
            break
        if (N - (A * na + B * nb)) % C == 0:
            nc = (N - (A * na + B * nb)) // C
            ans = min(ans, na + nb + nc)
print(ans)
