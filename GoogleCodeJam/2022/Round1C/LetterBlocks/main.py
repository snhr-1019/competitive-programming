from itertools import permutations


def is_mega(s):
    cur = s[0]
    appeared = set()
    for i in range(1, len(s)):
        if s[i] == cur:
            continue

        if s[i] in appeared:
            return False

        appeared.add(cur)
        cur = s[i]
    return True


def solve():
    n = int(input())
    S = list(input().split())
    for v in permutations(S):
        s = "".join(v)
        if is_mega(s):
            return s
    return "IMPOSSIBLE"


T = int(input())

for t in range(T):
    ans = solve()
    print(f'Case #{t + 1}: {ans}')
