from collections import defaultdict

N, C = map(int, input().split())

x = defaultdict(list)
min_day = 10 ** 9 + 1
max_day = 0
for i in range(N):
    ai, bi, ci = map(int, input().split())
    min_day = min(min_day, ai)
    max_day = max(max_day, bi)
    x[ai].append(ci)
    x[bi + 1].append(-1 * ci)

day_cost = 0
cost_sum = 0
days = [0] + sorted(x.keys())
for i in range(1, len(days)):
    cost_sum += min(day_cost, C) * (days[i] - days[i - 1])

    for cost in x[days[i]]:
        day_cost += cost

print(cost_sum)
