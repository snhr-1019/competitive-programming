from itertools import permutations


def solve(case):
    n = int(input())
    f = [0] + list(map(int, input().split()))
    p = [0] + list(map(int, input().split()))

    set_p = set(p)
    initiators = []
    for i in range(1, n + 1):
        if i not in set_p:
            initiators.append(i)

    ans = 0
    for v in permutations(initiators):
        score = 0
        used = [False] * (n + 1)
        for i in v:
            cur = i
            score_i = 0
            while True:
                score_i = max(score_i, f[cur])
                used[cur] = True

                nxt = p[cur]
                if nxt == 0 or used[nxt]:
                    break
                else:
                    cur = nxt
            score += score_i
        ans = max(score, ans)


    print(f'Case #{case}: {ans}')


t = int(input())

for i in range(t):
    solve(i + 1)
