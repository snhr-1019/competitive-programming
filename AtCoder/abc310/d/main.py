import pypyjit

pypyjit.set_param('max_unroll_recursion=-1')

n, t, m = map(int, input().split())
ab = set()

dp = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    ab.add(frozenset({a, b}))

teams = [set() for _ in range(t)]
ans = 0


def is_ok(i, team):
    for mem in team:
        if {i, mem} in ab:
            return False
    return True


def dfs(i):
    global teams
    global ans

    if i == n:
        if all(len(ti) > 0 for ti in teams):
            ans += 1
        return

    for j in range(t):
        first_empty = False
        if len(teams[j]) == 0:
            first_empty = True

        if is_ok(i, teams[j]):
            teams[j].add(i)
            dfs(i + 1)
            teams[j].remove(i)

        if first_empty:
            break


dfs(0)
print(ans)
