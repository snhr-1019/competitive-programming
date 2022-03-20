n = int(input())
used = [False] * (2 * n + 10)
for i in range(n + 1):
    for j in range(1, 2 * n + 10):
        if not used[j]:
            print(j, flush=True)
            used[j] = True
            break
    k = int(input())
    if k == 0:
        exit()
    used[k] = True
