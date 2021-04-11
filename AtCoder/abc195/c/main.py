N = int(input())

ans = 0
i = 1
while True:
    start = 10 ** (3 * (i - 1))
    end = 10 ** (3 * i) - 1
    if N < end:
        ans += (i - 1) * (N - start + 1)
        print(ans)
        exit()
    else:
        ans += (i - 1) * (end - start + 1)
        i += 1
