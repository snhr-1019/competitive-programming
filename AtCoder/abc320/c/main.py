from itertools import permutations

m = int(input())
s = [input() * 3 for _ in range(3)]

ans = 10 ** 9
for num in range(10):
    for v in permutations([0, 1, 2]):
        time = -1
        reel = 0
        for cur in range(3 * m):
            if s[v[reel]][cur] == str(num):
                reel += 1
            if reel >= 3:
                time = cur
                break
        if reel == 3:
            ans = min(ans, time)

if ans == 10 ** 9:
    print(-1)
else:
    print(ans)
