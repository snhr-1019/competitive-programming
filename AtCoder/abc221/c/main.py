from itertools import permutations

N = input()

ans = 0
for p in permutations(list(N)):
    # 区切る位置
    for i in range(len(N) - 1):
        if p[0] == 0 or p[i + 1] == 0:
            continue
        a = int("".join(p[0:i + 1]))
        b = int("".join(p[i + 1:len(N)]))
        ans = max(ans, a * b)
print(ans)
